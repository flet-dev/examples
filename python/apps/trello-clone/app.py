import logging
import os
from board import Board
import flet
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
    Text,
    TextButton,
    IconButton,
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
# from dotenv import dotenv_values

# config = dotenv_values(".env.dev")

# trello app
# MVP  - Boards -> Lists -> Cards
# Views - Different views of boards (timeline, table, etc.)
# Boards contain a hash of board_lists (kept as horizontal/vertical tuples), therefore manage those lists (addition, deletion, editing, etc.)
# BoardLists contain Lists of cards, therefore manage those cards (addition, deletion, checked state etc.)


class TrelloApp:
    def __init__(self, page: Page):
        self.page = page

        self.page.on_route_change = self.route_change
        self.sidebar = Sidebar(self, page)
        self.boards = [
            Board(self, "Empty Board")
        ]
        # could either be all boards, settings, individual boards. - this is a list of controls
        self.pages = []
        # could be pages as above or edit panes (as in cards for ex.) - this is a list of slugs
        self.routes = []
        self.current_board_index: int = 0
        self.current_board = self.boards[self.current_board_index]
        self.all_board_cards = Row(controls=[Column([Text(value=b.identifier), IconButton(
            icon=icons.SETTINGS)], alignment="spaceEvenly") for b in self.boards])
        self.all_boards = Column([
            Row([Text(value="Your Boards", style="headlineMedium"), TextButton(
                "Add new board", icon=icons.ADD, on_click=self.add_board), ]),
            Row([TextField(hint_text="Search this board", border="none", autofocus=False, on_submit=self.search_boards,
                content_padding=padding.only(top=4, left=15), filled=False, suffix_icon=icons.SEARCH)]),
            self.all_board_cards
        ])
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
                        items=[
                            PopupMenuItem(text="Profile"),
                            PopupMenuItem(),  # divider
                            PopupMenuItem(
                                text="Synchronize"
                            )
                        ]
                    ),
                    margin=margin.only(left=50, right=25)
                )
            ],
        )

        self.toggle_nav_rail_button = IconButton(
            icon=icons.ARROW_CIRCLE_LEFT, icon_color=colors.BLACK38, selected=False,
            selected_icon=icons.ARROW_CIRCLE_RIGHT, on_click=self.toggle_nav_rail,
            right=15)

        self.page_divider = Stack([
            VerticalDivider(width=2),
            self.toggle_nav_rail_button,
        ], clip_behavior="none", width=40)

        self.members = Column([
            Text("Members area")
        ])
        # self.view = Row(
        #     [
        #         # self.appbar,
        #         self.sidebar,
        #         self.page_divider,
        #         self.current_board
        #     ],
        #     tight=True,
        #     expand=True,
        # )

    def start(self):
        self.page.go(self.page.route)

    # define all routes here
    # 'boards', 'members', 'board/:id', 'board/:id/:item', 'member/:id'

    def route_change(self, e):
        print("changed route: ", e.route)
        split_route = e.route.split('/')
        print("split route: ", split_route[1:])
        self.page.views.clear()
        self.page.views.append(
            View(
                "/",
                [
                    self.appbar,
                    Row([
                        self.sidebar,
                        self.page_divider,
                        self.all_boards
                    ], expand=True)
                ],
                bgcolor=colors.BLUE_GREY_200
            )
        )
        self.page.update()
        print("self.page.controls", self.page.controls)
        match split_route[1:]:
            case ["board", board_number]:
                self.sidebar.bottom_nav_change(int(board_number))
                print("append board number:", board_number)
                self.page.views.append(
                    View(
                        f"/board/{board_number}",
                        [
                            self.appbar,
                            Row([
                                self.sidebar,
                                self.page_divider,
                                self.boards[int(board_number)]
                            ], expand=True)
                        ],
                        bgcolor=colors.BLUE_GREY_200
                    )
                )
            case ["boards"]:
                self.sidebar.top_nav_change(0)
                print("append boards")
                self.page.views.append(
                    View(
                        "/boards",
                        [
                            self.appbar,
                            Row([
                                self.sidebar,
                                self.page_divider,
                                self.all_boards
                            ], expand=True)
                        ],
                        bgcolor=colors.BLUE_GREY_200
                    )
                )
            case ["members"]:
                self.sidebar.top_nav_change(1)
                print("append members")
                self.page.views.append(
                    View(
                        "/members",
                        [
                            self.appbar,
                            Row([
                                self.sidebar,
                                self.page_divider,
                                self.members
                            ], expand=True)
                        ],
                        bgcolor=colors.BLUE_GREY_200
                    )
                )
        self.page.update()

    def update(self):
        self.current_board = self.boards[self.current_board_index]
        self.page.update()
        # self.view.update()

    def board_name_focus(self, e):
        e.control.read_only = False
        e.control.border = "outline"
        e.control.update()

    def board_name_blur(self, e):
        e.control.read_only = True
        e.control.border = "none"
        e.control.update()

    def toggle_nav_rail(self, e):
        print("hide nav_rail")
        # self.nav_rail_visible = not self.nav_rail_visible
        # self.view.visible = not self.view.visible
        self.sidebar.visible = not self.sidebar.visible
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        # self.view.update()
        # self.set_navigation_content()
        self.page.update()

    def nav_rail_change(self, e):
        self.current_board_index = e.control.selected_index
        if self.current_board in self.view.controls:
            self.current_board.visible = False
        self.current_board = self.boards[e.control.selected_index]
        self.current_board.visible = True
        # self.view.controls.append(self.current_board)
        # print("Selected destination: ", e.control.selected_index)
        self.view.update()

    def add_board(self, e):
        def close_dlg(e):
            self.create_new_board(e)
            dialog.open = False
            self.page.update()
        dialog = AlertDialog(
            title=Text("Name your new board"),
            content=Column(
                [TextField(label="New Board Name", on_submit=close_dlg)], tight=True),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def create_new_board(self, e):

        self.sidebar.destinations.append(
            NavigationRailDestination(
                # padding=padding.all(5),
                # label_content=Text(e.control.value),
                label_content=TextField(
                    # label="Full name",
                    hint_text=f"{e.control.value}",
                    read_only=True,
                    on_focus=self.board_name_focus,
                    on_blur=self.board_name_blur,
                    border="none",
                    height=50,
                    width=150,
                    text_align="start"

                ),
                label=e.control.value,
                selected_icon=icons.CHEVRON_RIGHT_ROUNDED
            )
        )
        new_board = Board(self, e.control.value)
        self.boards.append(new_board)
        # self.view.controls.remove(self.boards[self.current_board_index])
        self.boards[self.current_board_index].visible = False
        self.current_board_index = len(self.sidebar.destinations) - 1
        print("from createNewBoard - current_board_index: ",
              self.current_board_index)

        self.view.controls.append(self.boards[self.current_board_index])
        self.sidebar.selected_index = self.current_board_index
        self.update()

    def search_boards(self, e):
        "TODO"


if __name__ == "__main__":

    def main(page: Page):

        def search_app(e):
            "TODO"

        page.title = "Flet Trello clone"
        # page.bgcolor = colors.LIGHT_GREEN_400
        page.theme = theme.Theme(
            color_scheme_seed="green", font_family="Verdana")
        page.fonts = {
            "Pacifico": "/Pacifico-Regular.ttf"
        }
        page.update()
        app = TrelloApp(page)
        app.start()

    print("flet version: ", flet.version.version)
    flet.app(target=main, assets_dir="assets", view=flet.WEB_BROWSER)
