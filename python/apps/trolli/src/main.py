from board import Board
import os
import flet
from flet.buttons import RoundedRectangleBorder
from flet.auth.providers.auth0_oauth_provider import Auth0OAuthProvider
from flet.security import decrypt, encrypt
from flet import (
    UserControl,
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
    TemplateRoute,
)
from user import User
from data_store import DataStore
from memory_store import InMemoryStore
from app_layout import AppLayout


class TrelloApp(UserControl):
    def __init__(self, page: Page, store: DataStore):
        super().__init__()
        self.page = page
        self.store: DataStore = store
        self.page.on_route_change = self.route_change
        self.boards = self.store.get_boards()
        self.login_profile_button = PopupMenuItem(
            text="Log in", on_click=self.login)
        self.appbar_items = [
            self.login_profile_button,
            PopupMenuItem(),  # divider
            PopupMenuItem(text="Settings")
        ]
        self.appbar = AppBar(
            leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=Text(f"Trolli", font_family="Pacifico",
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
        self.encryption_key = os.getenv("TROLLI_ENCRYPTION_KEY")
        self.provider = Auth0OAuthProvider(
            domain="dev-j3wnirdjarxj51uz.us.auth0.com",
            client_id=os.getenv("AUTH0_CLIENT_ID"),
            client_secret=os.getenv("AUTH0_CLIENT_SECRET"),
            redirect_url="http://localhost:8088/api/oauth/redirect",
        )

        page.on_login = self.on_login
        self.page.update()

    # def login_click(self, e):

    def build(self):
        self.layout = AppLayout(self, self.page, self.store,
                                tight=True, expand=True, vertical_alignment="start")
        return self.layout

    def on_login(self, e):
        if e.error:
            raise Exception(e.error)

        jt = self.page.auth.token.to_json()
        ejt = encrypt(jt, self.encryption_key)
        self.page.client_storage.set("trolli_token", ejt)

        self.set_login_state()
        print("self.page.auth.user: ", self.page.auth.user)
        self.page.update()

    def set_login_state(self):
        print("set_login_state")
        self.layout.sidebar.set_workspace_user(self.page.auth.user["nickname"])
        if self.login_profile_button.text == "Log in":
            self.login_profile_button.text = "Log out"
        else:
            self.login_profile_button.text = "Log in"

    def initialize(self):
        self.page.views.clear()
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
        # create an initial board for demonstration if no boards
        if len(self.boards) == 0:
            self.create_new_board("My First Board")
        self.page.go("/")

    def login(self, e):

        saved_token = None
        ejt = self.page.client_storage.get("trolli.token")
        if ejt:
            saved_token = decrypt(ejt, self.encryption_key)
        if e is not None or saved_token is not None:
            self.page.login(self.provider, saved_token=saved_token)

    def route_change(self, e):
        troute = TemplateRoute(self.page.route)
        if troute.match("/"):
            self.page.go("/boards")
        elif troute.match("/board/:id"):
            if int(troute.id) > len(self.store.get_boards()):
                self.page.go("/")
                return
            self.layout.set_board_view(int(troute.id))
        elif troute.match("/boards"):
            self.layout.set_all_boards_view()
        elif troute.match("/members"):
            self.layout.set_members_view()
        self.page.update()

    def add_board(self, e):

        def close_dlg(e):
            if (hasattr(e.control, "text") and not e.control.text == "Cancel") or (type(e.control) is TextField and e.control.value != ""):
                self.create_new_board(dialog_text.value)
            dialog.open = False
            self.page.update()

        def textfield_change(e):
            if dialog_text.value == "":
                create_button.disabled = True
            else:
                create_button.disabled = False
            self.page.update()

        dialog_text = TextField(label="New Board Name",
                                on_submit=close_dlg, on_change=textfield_change)
        create_button = ElevatedButton(
            text="Create", bgcolor=colors.BLUE_200, on_click=close_dlg, disabled=True)
        dialog = AlertDialog(
            title=Text("Name your new board"),
            content=Column([
                dialog_text,
                Row([
                    ElevatedButton(
                        text="Cancel", on_click=close_dlg),
                    create_button
                ], alignment="spaceBetween")
            ], tight=True),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
        dialog_text.focus()

    def create_new_board(self, board_name):
        new_board = Board(self, self.store, board_name)
        self.store.add_board(new_board)
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
        app = TrelloApp(page, InMemoryStore())

        page.add(app)
        page.update()
        app.initialize()

    flet.app(target=main, port=8088,
             assets_dir="../assets", view=flet.WEB_BROWSER)
