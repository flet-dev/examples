from board import Board
import flet
from flet.buttons import RoundedRectangleBorder
from flet import (
    View,
    AlertDialog,
    Column,
    Row,
    Container,
    Icon,
    Page,
    Text,
    ElevatedButton,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    TextField,
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
#from memory_store import InMemoryStore
from memory_store import store
from app_layout import AppLayout


class TrelloApp:
    def __init__(self, page: Page):
        #self._lock = threading.Lock()
        self.page = page
        #self.user = user
        self.store: DataStore = store
        self.page.on_route_change = self.route_change
        #self.sidebar = Sidebar(self, page)
        self.boards = self.store.get_boards()

        self.login_profile_button = PopupMenuItem(
            text="Log in", on_click=self.login)
        self.appbar_items = [
            self.login_profile_button,
            PopupMenuItem(),  # divider
            PopupMenuItem(
                text="Data snapshot", on_click=self.store.data_snapshot
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
        self.page.appbar = self.appbar
        self.page.update()
        self.layout = AppLayout(self, self.page, self.store,
                                tight=True, expand=True, vertical_alignment="start")

    def initialize(self):
        self.page.views.append(
            View(
                "/",
                [
                    self.appbar,
                    self.layout
                ],
                padding=padding.all(0),
                bgcolor=colors.BLUE_GREY_200
            )
        )
        self.page.update()
        # create an initial board for demonstration
        self.create_new_board("My First Board")
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

    def route_change(self, e):
        #print("changed route: ", e.route)
        split_route = e.route.split('/')
        match split_route[1:]:
            case[""]:
                self.page.go("/boards")

            case ["board", board_number]:
                if int(board_number) > len(self.store.get_boards()):
                    self.page.go("/")
                    return
                self.layout.set_board_view(int(board_number))

            case ["boards"]:
                self.layout.set_all_boards_view()

            case ["members"]:
                self.layout.set_members_view()

        self.page.update()

    def add_board(self, e):
        def close_dlg(e):
            if (hasattr(e.control, "text") and not e.control.text == "Cancel") or type(e.control) is TextField:
                self.create_new_board(dialog_text.value)
            dialog.open = False
            self.page.update()
        dialog_text = TextField(label="New Board Name", on_submit=close_dlg)
        dialog = AlertDialog(
            title=Text("Name your new board"),
            content=Column([
                dialog_text,
                Row([
                    ElevatedButton(
                        text="Cancel", on_click=close_dlg),
                    ElevatedButton(
                        text="Create", bgcolor=colors.BLUE_200, on_click=close_dlg)
                ], alignment="spaceBetween")
            ], tight=True),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def create_new_board(self, board_name):
        new_board = Board(self, board_name)
        self.store.add_board(new_board)
        #self.layout.active_view = new_board
        self.layout.hydrate_all_boards_view()

    def delete_board(self, e):
        self.store.remove_board(e.control.data)
        self.layout.set_all_boards_view()


if __name__ == "__main__":

    def main(page: Page):

        page.title = "Flet Trello clone"
        page.padding = 0
        page.theme = theme.Theme(
            font_family="Verdana")
        page.theme.page_transitions.windows = "cupertino"
        page.fonts = {
            "Pacifico": "/Pacifico-Regular.ttf"
        }
        page.bgcolor = colors.BLUE_GREY_200
        page.update()
        app = TrelloApp(page)
        app.initialize()
        page.update()

    #print("flet version: ", flet.version.version)
    #print("flet path: ", flet.__file__)

    flet.app(target=main, assets_dir="assets", view=flet.WEB_BROWSER)
