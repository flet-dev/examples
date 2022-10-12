from board import Board
import flet
from flet.buttons import RoundedRectangleBorder
from flet import (
    View,
    AlertDialog,
    Column,
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
from memory_store import InMemoryStore
from app_layout import AppLayout


class TrelloApp:
    def __init__(self, page: Page, store: DataStore, user=None):
        #self._lock = threading.Lock()
        self.page = page
        self.user = user
        self.store = store
        #self.page.on_resize = self.page_resize
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
        self.page.appbar = self.appbar
        self.page.update()
        self.layout = AppLayout(self, self.page, self.store,
                                tight=True, expand=True, vertical_alignment="start")

    def start(self):
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
        #print("split route: ", split_route[1:])
        #print("self.page.controls", self.page.controls)
        match split_route[1:]:
            case[""]:
                self.page.go("/boards")

            case ["board", board_number]:
                if int(board_number) > len(self.store.get_boards()):
                    self.page.go("/")
                    return
                self.current_board = self.store.get_boards()[int(board_number)]
                self.layout.set_board_view(int(board_number))

            case ["boards"]:
                self.layout.set_all_boards_view()
                self.current_board = None

            case ["members"]:
                self.layout.set_members_view()
                self.current_board = None

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
        self.current_board = new_board
        self.layout.active_view = new_board
        self.layout.populate_all_boards_view()

    def delete_board(self, e):
        self.current_board = None
        self.store.remove_board(e.control.data)
        self.layout.set_all_boards_view()

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
