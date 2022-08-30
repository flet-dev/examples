from board import Board
import flet
from flet import (
    UserControl,
    AlertDialog,
    Column,
    Container,
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
    margin,
    border,
    slugify
)


class Sidebar(UserControl):

    def __init__(self, app, routes):
        super().__init__()
        self.app = app
        #self.current_nav_item = 0
        self.routes = routes
        self.workspace_nav_items = [
            NavigationRailDestination(
                label_content=Text("Boards"),
                selected_icon=icons.BOOK_OUTLINED
            ),
            NavigationRailDestination(
                label_content=Text("Members"),
                selected_icon=icons.PERSON
            ),
            Divider()
        ]
        self.nav_rail = NavigationRail(
            selected_index=0,
            label_type="none",
            on_change=self._nav_change,
            destination=self.workspace_nav_items
        )
        self.nav_drawer_toggle = IconButton(icons.ARROW_BACK)

    def build(self):
        self.view = Column([
            Row([
                Text("Workspace"),
                Container(content=self.nav_drawer_toggle,
                          alignment=alignment.center_right)
            ]),
            Divider(),
            self.nav_rail
        ])
        return self.view

    def select_board(self, board_number):
        self.nav_rail.selected_index = board_number

    def toggle_navigation(self, event=None):
        self._panel_visible = not self._panel_visible
        self.set_navigation_content()
        self.page.update()

    def _nav_change(self, e):
        index = e.control.selected_index
        self.page.route = self.routes[index]
        self.app.current_board = self.app.boards[index]

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
        self.app.page.dialog = dialog
        dialog.open = True
        self.app.page.update()

    def create_new_board(self, e):

        self.sidebar.destinations.append(
            NavigationRailDestination(
                # padding=padding.all(5),
                # label_content=Text(e.control.value),
                label_content=TextField(
                    #label="Full name",
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
