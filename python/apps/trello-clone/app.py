import threading
import logging
import os
from board import Board
import flet
from flet.buttons import RoundedRectangleBorder
from flet import (
    UserControl,
    View,
    AlertDialog,
    Column,
    Container,
    Stack,
    GridView,
    Icon,
    IconButton,
    Page,
    Row,
    SnackBar,
    Card,
    Text,
    TextButton,
    IconButton,
    ElevatedButton,
    ButtonStyle,
    FloatingActionButton,
    NavigationRail,
    NavigationRailDestination,
    VerticalDivider,
    Divider,
    AppBar,
    Checkbox,
    ListTile,
    PopupMenuButton,
    PopupMenuItem,
    TextField,
    Switch,
    alignment,
    border_radius,
    colors,
    icons,
    padding,
    theme,
    margin,
    border
)
from sidebar import Sidebar
from user import User
from data_store import DataStore
from memory_store import InMemoryStore

# from dotenv import dotenv_values

# config = dotenv_values(".env.dev")

# trello app
# MVP  - Boards -> Lists -> Cards
# Views - Different views of boards (timeline, table, etc.)
# Boards contain a hash of board_lists (kept as horizontal/vertical tuples), therefore manage those lists (addition, deletion, editing, etc.)
# BoardLists contain Lists of cards, therefore manage those cards (addition, deletion, checked state etc.)


class TrelloApp:
    def __init__(self, page: Page, store: DataStore, user=None):
        #self._lock = threading.Lock()
        self.page = page
        self.user = user
        self.store = store
        self.page.on_resize = self.page_resize
        self.page.on_route_change = self.route_change
        self.sidebar = Sidebar(self, page)
        self.boards = self.store.get_boards()
        self.current_board_index: int | None = None
        self.current_board = None if self.current_board_index == None else self.boards[
            self.current_board_index]

        self.login_profile_button = PopupMenuItem(
            text="Log in", on_click=self.login)
        self.appbar_items = [
            self.login_profile_button,
            PopupMenuItem(),  # divider
            PopupMenuItem(
                text="Synchronize"
            )
        ]
        self.appbar = AppBar(
            leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=Text("Trolli", font_family="Pacifico", size=32),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                Container(
                    content=PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=margin.only(left=50, right=25)
                )
            ],
        )

        self.toggle_nav_rail_button = IconButton(
            icon=icons.ARROW_CIRCLE_LEFT, icon_color=colors.BLUE_GREY_400, selected=False,
            selected_icon=icons.ARROW_CIRCLE_RIGHT, on_click=self.toggle_nav_rail, right=5)

        self.page_divider = Stack([
            VerticalDivider(width=2),
            self.toggle_nav_rail_button,
        ], clip_behavior="none", width=30)
        self.page.appbar = self.appbar
        self.page.update()
        self.members_view = Text("members view", visible=False)
        self.all_boards_view = Column([
            Row([
                Text(value="Your Boards", style="headlineMedium", expand=True),
                Container(
                    TextButton(
                        "Add new board",
                        icon=icons.ADD,
                        on_click=self.add_board,
                        style=ButtonStyle(
                            bgcolor={
                                "": colors.BLUE_200,
                                "hovered": colors.BLUE_400
                            },
                            shape={
                                "": RoundedRectangleBorder(radius=3)
                            }
                        )
                    ),

                    padding=padding.only(right=50))
            ]),
            Row([
                TextField(hint_text="Search all boards", autofocus=False, content_padding=padding.only(left=10),
                          width=200, height=40, on_submit=self.search_boards, text_size=12,
                          border_color=colors.BLACK26, focused_border_color=colors.BLUE_ACCENT, suffix_icon=icons.SEARCH)
            ])
        ], expand=True)
        self.view = Row([
            self.sidebar,
            self.page_divider,
            self.all_boards_view,
            self.members_view
        ], tight=True, expand=True)

    def start(self):
        # some initialization
        self.create_new_board("my board")
        self.sidebar.top_nav_rail.selected_index = 0
        self.page.views.append(
            View(
                "/",
                [
                    self.appbar,
                    self.view
                ],
                bgcolor=colors.BLUE_GREY_200
            )
        )
        # self.page.go("/")
        # self.page.update()
        #print("self.boards: ", self.boards)

    def login(self, e):

        def close_dlg(e):
            if user_name.value == "" or password.value == "":
                user_name.error_text = "Please provide username"
                password.error_text = "Please provide password"
                self.page.update()
                return
            else:
                print("name and password: ", user_name.value, password.value)
                user = User(user_name.value, password.value)
                if user not in self.user_repo.list():
                    self.user_repo.add(user)
                self.user = user_name.value
                self.page.client_storage.set("current_user", user_name.value)

            dialog.open = False
            self.appbar_items[0] = PopupMenuItem(
                text=f"{self.page.client_storage.get('current_user')}'s Profile")
            self.page.update()
        user_name = TextField(label="User name")
        password = TextField(label="Password", password=True)
        dialog = AlertDialog(
            title=Text("Please enter your login credentials"),
            content=Column([
                user_name,
                password,
                ElevatedButton(text="Login", on_click=close_dlg),
            ], tight=True),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def page_resize(self, e):
        new_width = (self.page.width -
                     330) if self.sidebar.visible else (self.page.width - 30)
        for board in self.boards:
            board.resize(new_width, self.page.height)

    def route_change(self, e):
        #print("changed route: ", e.route)
        split_route = e.route.split('/')
        #print("split route: ", split_route[1:])
        #print("self.page.controls", self.page.controls)
        match split_route[1:]:
            case[""]:
                self.page.go("/boards")

            case ["board", board_number]:
                #print("append board number:", board_number)
                self.current_board = self.boards[int(board_number)]
                if int(board_number) > len(self.boards):
                    #print("board number out of range")
                    self.page.go("/")
                    return
                for ctrl in self.view.controls[2:4]:
                    ctrl.visible = False
                for i, ctrl in enumerate(self.view.controls[4:]):
                    ctrl.visible = int(board_number) == i
                    #print("ctrl, i, ctrl.visible: ", ctrl, i, ctrl.visible)
                self.sidebar.bottom_nav_rail.selected_index = int(board_number)
                self.sidebar.top_nav_rail.selected_index = None
                self.sidebar.update()
            case ["boards"]:
                for ctrl in self.view.controls[4:]:
                    ctrl.visible = False
                # set all controls in app.view to visible=False except this index
                for i, ctrl in enumerate(self.view.controls[2:4]):
                    ctrl.visible = i == 0
                # self.sidebar.top_nav_change(0)
                self.sidebar.top_nav_rail.selected_index = 0
                self.sidebar.bottom_nav_rail.selected_index = None
                self.sidebar.update()
                self.populate_all_boards_view()
            case ["members"]:
                self.sidebar.top_nav_change(1)
                print("append members")
                for ctrl in self.view.controls[4:]:
                    ctrl.visible = False
                # set all controls in app.view to visible=False except this index
                for i, ctrl in enumerate(self.view.controls[2:4]):
                    ctrl.visible = i == 1
                self.sidebar.top_nav_rail.selected_index = 1
                self.sidebar.bottom_nav_rail.selected_index = None
                self.sidebar.update()
        self.page.update()

    def update(self):
        self.boards = self.store.get_boards()
        #self.current_board = self.boards[self.current_board_index]
        self.page.update()
        # self.view.update()

    def populate_all_boards_view(self):
        self.all_boards_view.controls[-1] = Row([
            Container(content=Row([Container(content=Text(value=b.identifier), data=b, expand=True, on_click=self.board_click), Container(
                content=PopupMenuButton(
                    items=[
                        PopupMenuItem(
                            content=Text(value="Delete...", style="labelMedium",
                                         text_align="center"),
                            on_click=self.delete_board, data=b),
                        PopupMenuItem(),
                        PopupMenuItem(
                            content=Text(value="Archive...", style="labelMedium",
                                         text_align="center"),
                        )
                    ]
                ),

                border_radius=border_radius.all(3)
            )], alignment="spaceBetween"),
                border=border.all(1, colors.BLACK38),
                border_radius=border_radius.all(5),
                bgcolor=colors.WHITE60,
                padding=padding.all(10),
                width=250,
                # on_click=self.board_click,
                data=b
            ) for b in self.store.get_boards()
        ], wrap=True)

    def board_click(self, e):
        self.sidebar.bottom_nav_change(self.boards.index(e.control.data))

    def toggle_nav_rail(self, e):
        self.sidebar.visible = not self.sidebar.visible
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        # for board in self.boards:
        #     board.resize(self.page.width, self.page.height)
        new_width = (self.page.width -
                     330) if self.sidebar.visible else (self.page.width - 30)
        self.current_board.resize(new_width, self.page.height)
        self.page.update()

    # def nav_rail_change(self, e):
    #     self.current_board_index = e.control.selected_index
    #     if self.current_board in self.view.controls:
    #         self.current_board.visible = False
    #     self.current_board = self.boards[e.control.selected_index]
    #     self.current_board.visible = True
    #     # self.view.controls.append(self.current_board)
    #     # print("Selected destination: ", e.control.selected_index)
    #     self.view.update()

    def add_board(self, e):
        def close_dlg(e):
            self.create_new_board(e.control.value)
            dialog.open = False
            self.page.update()
        dialog = AlertDialog(
            title=Text("Name your new board"),
            content=Column([
                TextField(label="New Board Name", on_submit=close_dlg)
            ], tight=True),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def create_new_board(self, board_name):
        new_board = Board(self, board_name)
        # self.boards.append(new_board)
        self.store.add_board(new_board)
        self.view.controls.append(new_board)
        # self.view.update()
        #print("self.view.controls: ", self.view.controls)
        self.populate_all_boards_view()
        self.sidebar.add_board_destination(board_name)
        # self.page.update()
        self.update()

    def delete_board(self, e):
        print("e.control.data: ", e.control.data)
        i = self.store.get_boards().index(e.control.data)
        # self.boards.remove(e.control.data)
        self.store.remove_board(e.control.data)
        # self.view.controls.remove(e.control.data)
        self.sidebar.remove_board_destination(i)
        self.populate_all_boards_view()
        self.page.update()

    def search_boards(self, e):
        pass


if __name__ == "__main__":

    def main(page: Page):

        page.title = "Flet Trello clone"
        page.theme = theme.Theme(
            # color_scheme_seed="green",
            font_family="Verdana")
        page.theme.page_transitions.windows = "cupertino"
        page.fonts = {
            "Pacifico": "/Pacifico-Regular.ttf"
        }
        page.bgcolor = colors.BLUE_GREY_200
        store = InMemoryStore(page)
        app = TrelloApp(page, store)
        app.start()
        # page.add(app.view)
        page.update()

    #print("flet version: ", flet.version.version)
    #print("flet path: ", flet.__file__)

    flet.app(target=main, assets_dir="assets", view=flet.WEB_BROWSER)
