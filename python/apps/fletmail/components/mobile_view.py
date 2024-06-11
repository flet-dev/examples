import flet as ft
from components.app_view import AppView
from components.new_message_view import NewMessageMobileView
from model.messages import messages


class MobileView(AppView):
    def __init__(self):
        super().__init__()
        self.nav_bar_destinations = [
            ft.NavigationDestination(
                label="Mail",
                icon=ft.icons.MAIL_OUTLINED,
            ),
            ft.NavigationDestination(
                label="Chat",
                icon=ft.icons.CHAT_BUBBLE_OUTLINE,
            ),
            ft.NavigationDestination(
                label="Meet",
                icon=ft.icons.VIDEO_CHAT_OUTLINED,
            ),
        ]

        self.open_menu_button = ft.IconButton(
            icon=ft.icons.MENU, on_click=self.open_close_secondary_menu
        )
        self.navigation_bar = ft.NavigationBar(
            destinations=self.nav_bar_destinations, on_change=self.nav_bar_changed
        )

        self.floating_action_button = ft.FloatingActionButton(
            icon=ft.icons.CREATE, text="Compose", on_click=self.compose_clicked
        )

        self.drawer = ft.NavigationDrawer(
            controls=[
                ft.TextButton("Inbox"),
                ft.TextButton("Starred"),
                ft.TextButton("Spam"),
            ]
        )
        self.appbar = ft.AppBar(leading=self.open_menu_button)

        self.mail_view = ft.ListView(controls=self.get_messages(), expand=True)
        self.chat_view = ft.Text("Chat View")
        self.meet_view = ft.Text("Meet View")

        self.controls = [self.mail_view, self.chat_view, self.meet_view]

    def nav_bar_changed(self, e):
        print(f"Selected action: {e.control.selected_index}")
        if e.control.selected_index == 0:
            print("Open Mail Menu")
            self.display_inbox()
        if e.control.selected_index == 1:
            print("Open Chat Menu")
            self.display_chat()
        if e.control.selected_index == 1:
            print("Open Meet Menu")
            self.display_meet()

    def open_close_secondary_menu(self, e):
        print("Open secondary menu")
        self.drawer.open = True
        self.drawer.update()

    def compose_clicked(self, e):
        print("Open new message dialog")
        self.page.views.append(NewMessageMobileView())
        self.page.update()

    def get_messages(self):
        messages_list = []
        for message in messages:
            messages_list.append(
                ft.ListTile(
                    leading=ft.CircleAvatar(content=ft.Text("JS")),
                    title=ft.Text(message["author"]),
                    subtitle=ft.Text(message["title"]),
                    trailing=ft.Text(message["date"]),
                )
            )
        return messages_list

    def display_inbox(self):
        print("Display inbox")
        self.mail_view.visible = True
        self.chat_view.visible = False
        self.meet_view.visible = False
        self.page.go("/inbox")

    def display_chat(self):
        print("Display chat")
        self.mail_view.visible = False
        self.chat_view.visible = True
        self.meet_view.visible = False
        self.page.go("/chat")

    def display_meet(self):
        print("Display meet")
        self.mail_view.visible = False
        self.chat_view.visible = False
        self.meet_view.visible = True
        self.page.go("/meet")
