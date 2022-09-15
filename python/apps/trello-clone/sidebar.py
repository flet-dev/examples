from board import Board
import flet
from flet import (
    UserControl,
    AlertDialog,
    Column,
    Container,
    IconButton,
    Page,
    Row,
    Text,
    IconButton,
    NavigationRail,
    NavigationRailDestination,
    VerticalDivider,
    Divider,
    TextField,
    alignment,
    border_radius,
    colors,
    icons,
    padding,
    margin,
    border,
    slugify
)


class Sidebar(UserControl):

    def __init__(self, app, page):
        super().__init__()
        self.app = app
        self.page = page
        self.nav_rail_visible = True
        self.top_nav_items = [
            NavigationRailDestination(
                label_content=Text("Boards"),
                label="Boards",
                icon=icons.BOOK_OUTLINED,
                selected_icon=icons.BOOK_OUTLINED
            ),
            NavigationRailDestination(
                label_content=Text("Members"),
                label="Members",
                icon=icons.PERSON,
                selected_icon=icons.PERSON
            ),

        ]
        self.bottom_nav_items = []
        self.top_nav_rail = NavigationRail(
            selected_index=None,
            label_type="all",
            on_change=self.top_nav_change,
            destinations=self.top_nav_items,
            extended=True,
            # expand=True,
            bgcolor=colors.BLUE_GREY,
            height=110
        )
        self.bottom_nav_rail = NavigationRail(
            selected_index=None,
            label_type="all",
            on_change=self.bottom_nav_change,
            # destinations=self.bottom_nav_items,
            extended=True,
            expand=True,
            bgcolor=colors.BLUE_GREY,
        )
        self.toggle_nav_rail_button = IconButton(icons.ARROW_BACK)

    def build(self):
        self.view = Container(
            content=Column([
                Row([
                    Text("Workspace"),
                    # Container(content=self.toggle_nav_rail_button,
                    #           alignment=alignment.center_right, on_click=self.toggle_nav_rail)
                ], alignment="spaceBetween"),
                # divider
                Container(
                    bgcolor=colors.BLACK26,
                    border_radius=border_radius.all(30),
                    height=1,
                    alignment=alignment.center_right,
                    width=220
                ),
                self.top_nav_rail,
                # divider
                Container(
                    bgcolor=colors.BLACK26,
                    border_radius=border_radius.all(30),
                    height=1,
                    alignment=alignment.center_right,
                    width=220
                ),
                self.bottom_nav_rail
            ], tight=True),
            padding=padding.all(10),
            margin=margin.all(0),
            width=250,
            expand=True,
            bgcolor=colors.BLUE_GREY,
            visible=self.nav_rail_visible,
        )
        return self.view

    def add_board_destination(self, board_name):
        self.bottom_nav_rail.destinations.append(
            NavigationRailDestination(
                label_content=TextField(
                    value=board_name,
                    hint_text=board_name,
                    text_size=12,
                    read_only=True,
                    on_focus=self.board_name_focus,
                    on_blur=self.board_name_blur,
                    border="none",
                    height=50,
                    width=150,
                    text_align="start",
                    data=len(self.bottom_nav_rail.destinations)
                ),
                label=board_name,
                selected_icon=icons.CHEVRON_RIGHT_ROUNDED,
                icon=icons.CHEVRON_RIGHT_OUTLINED
            )
        )
        self.app.populate_all_boards_view()
        # self.app.view.update()
        self.app.page.update()
        if len(self.bottom_nav_rail.destinations) > 1:
            print("call bottom_nav_change")
            self.bottom_nav_change(len(self.bottom_nav_rail.destinations) - 1)

    def remove_board_destination(self, board_index):
        del self.bottom_nav_rail.destinations[board_index]
        self.view.update()
        # self.page.update()

    def toggle_nav_rail(self, e):
        self.view.visible = not self.view.visible
        self.view.update()
        self.page.update()

    def board_name_focus(self, e):
        e.control.read_only = False
        e.control.border = "outline"
        e.control.update()

    def board_name_blur(self, e):
        print("e.control: ", e.control.data)
        self.app.boards[e.control.data].identifier = e.control.value
        self.app.populate_all_boards_view()
        e.control.read_only = True
        e.control.border = "none"
        e.control.update()
        self.page.update()

    def top_nav_change(self, e):
        index = e if (type(e) == int) else e.control.selected_index
        self.bottom_nav_rail.selected_index = None
        self.top_nav_rail.selected_index = index
        self.view.update()
        if index == 0:
            self.page.route = "/boards"
        elif index == 1:
            self.page.route = "/members"
        self.page.update()
        # self.page.go(f"/{slugify(route_name)}")

    def bottom_nav_change(self, e):
        print("bottom nav change")
        index = e if (type(e) == int) else e.control.selected_index
        self.top_nav_rail.selected_index = None
        self.bottom_nav_rail.selected_index = index
        self.page.route = f"/board/{index}"
        self.view.update()
        self.page.update()
        # self.page.go(f"/board/{index}")
