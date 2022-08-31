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
            expand=True,
            bgcolor=colors.BLUE_GREY,
            height=70
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
                    Container(content=self.toggle_nav_rail_button,
                              alignment=alignment.center_right, on_click=self.toggle_nav_rail)
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
        self.nav_rail_visible = not self.nav_rail_visible
        self.set_navigation_content()
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
        # this should call page change
        self.bottom_nav_rail.selected_index = None
        self.view.update()
        route_name = self.top_nav_items[e.control.selected_index].label
        self.page.go(f"/{slugify(route_name)}")

        # self.app.page_change(self.routes_index[e.control.selected_index])
        #self.page.route = self.routes[index]
        #self.app.current_board = self.app.boards[index]

    def bottom_nav_change(self, e):
        # this should call page change
        self.top_nav_rail.selected_index = None
        self.view.update()
        self.page.go(f"/board/{e.control.selected_index}")

        # self.app.page_change(self.routes_index[e.control.selected_index])
        #self.page.route = self.routes[index]
        #self.app.current_board = self.app.boards[index]

    # to be implemented on 'Boards' page
    # def add_board(self, e):
    #     def close_dlg(e):
    #         self.create_new_board(e)
    #         dialog.open = False
    #         self.page.update()
    #     dialog = AlertDialog(
    #         title=Text("Name your new board"),
    #         content=Column(
    #             [TextField(label="New Board Name", on_submit=close_dlg)], tight=True),
    #         on_dismiss=lambda e: print("Modal dialog dismissed!"),
    #     )
    #     self.page.dialog = dialog
    #     dialog.open = True
    #     self.page.update()

    def create_new_board(self, e):

        self.nav_rail.destinations.append(
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
        self.app.routes.append(slugify(e.control.value))
        self.routes_index[len(self.nav_rail.destinations)
                          ] = slugify(e.control.value)
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
