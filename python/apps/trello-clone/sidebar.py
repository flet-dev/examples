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
        self.routes_index = {}
        # self.current_nav_item = 0
        # self.routes = routes
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
        self.bottom_nav_items = [
            NavigationRailDestination(
                # padding=padding.all(5),
                # label_content=Text("Empty Board"),
                label="Your First Board",
                label_content=TextField(
                    #label="Your First Board",
                    hint_text="Your First Board",
                    read_only=True,
                    on_focus=self.board_name_focus,
                    on_blur=self.board_name_blur,
                    border="none",
                    text_size=12,
                    width=150,
                    height=50,
                    text_align="start"

                ),
                selected_icon=icons.CHEVRON_RIGHT_ROUNDED
            )
        ]
        self.top_nav_rail = NavigationRail(
            selected_index=None,
            label_type="all",
            on_change=self.top_nav_change,
            destinations=self.top_nav_items,
            extended=True,
            # expand=True,
            bgcolor=colors.BLUE_GREY,
            height=120
        )
        self.bottom_nav_rail = NavigationRail(
            selected_index=None,
            label_type="all",
            on_change=self.bottom_nav_change,
            destinations=self.bottom_nav_items,
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
                    bgcolor=colors.BLACK54,
                    border_radius=border_radius.all(30),
                    height=1,
                    # alignment=alignment.center_right,
                    width=250
                ),
                self.top_nav_rail,
                # divider
                Container(
                    bgcolor=colors.BLACK54,
                    border_radius=border_radius.all(30),
                    height=1,
                    # alignment=alignment.center_right,
                    width=250
                ),
                self.bottom_nav_rail
            ], tight=True),
            # content=self.nav_rail,
            padding=padding.all(10),
            margin=margin.all(0),
            width=250,
            expand=True,
            bgcolor=colors.BLUE_GREY,
            visible=self.nav_rail_visible,
        )
        return self.view
        # return self.nav_rail

    def select_page(self, index):
        self.navigation_rail.selected_index = index
        self.set_visible_content()

    def set_visible_content(self):
        self.page.route = self.routes[self.nav_rail.selected_index]

        pass

    def select_board(self, board_number):
        self.nav_rail.selected_index = board_number

    def toggle_nav_rail(self, e):
        self.view.visible = not self.view.visible
        self.view.update()
        # self.set_navigation_content()
        self.page.update()

    def board_name_focus(self, e):
        e.control.read_only = False
        e.control.border = "outline"
        e.control.update()

    def board_name_blur(self, e):
        e.control.read_only = True
        e.control.border = "none"
        e.control.update()

    def top_nav_change(self, e):
        index = e if (type(e) == int) else e.control.selected_index
        self.bottom_nav_rail.selected_index = None
        self.top_nav_rail.selected_index = index
        self.view.update()
        route_name = self.top_nav_items[index].label
        print("route_name: ", route_name)
        self.page.go(f"/{slugify(route_name)}")

    def bottom_nav_change(self, e):
        index = e if (type(e) == int) else e.control.selected_index
        self.top_nav_rail.selected_index = None
        self.bottom_nav_rail.selected_index = index
        self.view.update()
        self.page.go(f"/board/{index}")
