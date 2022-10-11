import threading
from board import Board
import flet
from flet.buttons import RoundedRectangleBorder
from flet import (
    Control,
    View,
    AlertDialog,
    Column,
    Container,
    Stack,
    Icon,
    IconButton,
    Page,
    Row,
    Text,
    TextButton,
    IconButton,
    ElevatedButton,
    ButtonStyle,
    VerticalDivider,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    TextField,
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


class AppLayout(Row):

    def __init__(
        self,
        page: Page,
        store: DataStore,
        active_view: Control,
        *args
    ):
        super.__init__(*args)
        self.page = page
        self.active_view = active_view
        self.toggle_nav_rail_button = IconButton(
            icon=icons.ARROW_CIRCLE_LEFT, icon_color=colors.BLUE_GREY_400, selected=False,
            selected_icon=icons.ARROW_CIRCLE_RIGHT, on_click=self.toggle_nav_rail)

        self.sidebar = Sidebar(self, page)
        self.controls = [self.sidebar,
                         self.toggle_nav_rail_button, self.active_view]

    def set_content(self, active_view: Control):
        self.controls[-1] = active_view
        pass


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
        self.current_board = None

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
            title=Text("Trolli", font_family="Pacifico",
                       size=32, text_align="start"),
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
            selected_icon=icons.ARROW_CIRCLE_RIGHT, on_click=self.toggle_nav_rail)

        self.page_divider = Stack([
            VerticalDivider(width=2),
            self.toggle_nav_rail_button,
        ], clip_behavior="none", width=30)
        self.page.appbar = self.appbar
        self.page.update()
        self.members_view = Text("members view", visible=False)
        self.all_boards_view = Column([
            Row([
                Container(
                    Text(value="Your Boards", style="headlineMedium"),
                    expand=True,
                    padding=padding.only(top=15)),
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

                    padding=padding.only(right=50, top=15))
            ]),
            Row([
                TextField(hint_text="Search all boards", autofocus=False, content_padding=padding.only(left=10),
                          width=200, height=40, on_submit=self.search_boards, text_size=12,
                          border_color=colors.BLACK26, focused_border_color=colors.BLUE_ACCENT, suffix_icon=icons.SEARCH)
            ])
        ], expand=True)

        self.view = Row([
            self.sidebar,
            self.toggle_nav_rail_button,
            self.all_boards_view,
            self.members_view
        ], tight=True, expand=True, vertical_alignment="start")

    def start(self):
        self.page.views.append(
            View(
                "/",
                [
                    self.appbar,
                    self.view
                ],
                padding=padding.all(0),
                bgcolor=colors.BLUE_GREY_200
            )
        )
        self.page.update()
        # create an initial board for demonstration
        self.create_new_board("My First Board")
        self.sidebar.top_nav_rail.selected_index = 0
        self.page.go("/")

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
                if user not in self.store.get_users():
                    self.store.add_user(user)
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
        for board in self.store.get_boards():
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
                self.current_board = self.store.get_boards()[int(board_number)]
                if int(board_number) > len(self.store.get_boards()):
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
                self.current_board = None
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

    def populate_all_boards_view(self):
        self.all_boards_view.controls[-1] = Row([
            Container(
                content=Row([
                    Container(
                        content=Text(value=b.identifier), data=b, expand=True, on_click=self.board_click),
                    Container(
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
                        padding=padding.only(right=-10),
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
        print("self.boards.index: ", self.store.get_boards().index(e.control.data))
        self.sidebar.bottom_nav_change(
            self.store.get_boards().index(e.control.data))

    def toggle_nav_rail(self, e):
        self.sidebar.visible = not self.sidebar.visible
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        new_width = (self.page.width -
                     330) if self.sidebar.visible else (self.page.width - 30)
        if self.current_board != None:
            self.current_board.resize(new_width, self.page.height)
        self.page.update()

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
        self.store.add_board(new_board)
        self.view.controls.append(new_board)
        self.current_board = new_board
        self.sidebar.sync_board_destinations()

        self.populate_all_boards_view()
        self.page.update()

    def delete_board(self, e):
        print("e.control.data: ", e.control.data)
        self.current_board = None
        self.store.remove_board(e.control.data)
        self.view.controls.remove(e.control.data)
        self.sidebar.sync_board_destinations()
        self.populate_all_boards_view()
        self.page.update()

    def search_boards(self, e):
        pass


if __name__ == "__main__":

    def main(page: Page):

        page.title = "Flet Trello clone"
        page.padding = 0
        page.theme = theme.Theme(
            # color_scheme_seed="green",
            font_family="Verdana")
        page.theme.page_transitions.windows = "cupertino"
        page.fonts = {
            "Pacifico": "/Pacifico-Regular.ttf"
        }
        page.bgcolor = colors.BLUE_GREY_200
        page.update()
        store = InMemoryStore()
        app = TrelloApp(page, store)
        app.start()
        page.update()

    #print("flet version: ", flet.version.version)
    #print("flet path: ", flet.__file__)

    flet.app(target=main, assets_dir="assets", view=flet.WEB_BROWSER)
