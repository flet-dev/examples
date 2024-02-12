import flet as ft

from data.chat import Chat, ChatMessage
from data.user import User
from views.chats_view import ChatView
from views.contacts_view import ContactsView
from views.settings_view import SettingsView


class Fletogram:
    def __init__(self, page):
        super().__init__()
        self.chats = []
        self.users = []
        self.page = page
        self.navigation_bar = ft.NavigationBar(
            selected_index=1,
            destinations=[
                ft.NavigationDestination(
                    icon=ft.icons.CONTACT_EMERGENCY,
                    label="Contacts",
                ),
                ft.NavigationDestination(
                    icon=ft.icons.CHAT,
                    label="Chats",
                ),
                ft.NavigationDestination(
                    icon=ft.icons.SETTINGS,
                    label="Settings",
                ),
            ],
            on_change=self.view_changed,
        )
        self.generate_users()
        self.generate_group_chats()
        self.generate_individual_chats()
        self.generate_tabs()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)

    def generate_tabs(self):
        self.tabs = [ContactsView(self), ChatView(self), SettingsView(self)]
        self.page.adaptive = True
        self.page.window_width = 393
        self.page.window_height = 852
        self.page.on_view_pop = self.view_pop
        self.page.views.clear()
        self.page.views.append(self.tabs[1])
        self.page.update()

    def view_changed(self, e):
        self.page.views.clear()
        self.page.views.append(self.tabs[self.navigation_bar.selected_index])
        self.page.update()

    def generate_users(self):
        self.users = [
            User(id=100, display_name="Inesa"),
            User(id=101, display_name="Feodor"),
            User(id=102, display_name="John"),
        ]
        self.logged_user = self.users[0]

    def generate_group_chats(self):

        self.chats = [
            Chat(
                fletogram=self,
                name="work",
                display_name="Flet developers",
                messages=[
                    ChatMessage(
                        author=self.users[0],
                        body="I have a question about adaptive design",
                        is_logged_user=True,
                    ),
                    ChatMessage(author=self.users[1], body="?", is_logged_user=False),
                    ChatMessage(
                        author=self.users[0],
                        body="What if it looks ugly?",
                        is_logged_user=True,
                    ),
                ],
            ),
            Chat(
                fletogram=self,
                name="Inesa",
                display_name="Inesa's stories",
                messages=[
                    ChatMessage(
                        author=self.users[0],
                        body="Inesa Message 1 title is very long and boring",
                        is_logged_user=True,
                    ),
                    ChatMessage(
                        author=self.users[0],
                        body="Inesa Message 1 title is very long and boring",
                        is_logged_user=True,
                    ),
                    ChatMessage(
                        author=self.users[0],
                        body="Inesa Message 1 title is very long and boring and wouldn't fit into one line it will also not fit into two lines unfortunately",
                        is_logged_user=True,
                    ),
                ],
            ),
            Chat(fletogram=self, name="Saved", display_name="My saved messages"),
        ]

    def generate_individual_chats(self):
        for user in self.users:
            self.chats.append(
                Chat(fletogram=self, name=user.id, display_name=user.display_name)
            )
