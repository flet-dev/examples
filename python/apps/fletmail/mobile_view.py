import flet as ft
from messages import messages
from new_message_view import NewMessageMobileView


class MobileView(ft.View):
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

        self.messages_list = ft.ListView(controls=self.get_messages(), expand=True)

        self.controls = [self.messages_list]

    def nav_bar_changed(self, e):
        print(f"Selected action: {e.control.selected_index}")
        if e.control.selected_index == 0:
            print("Open Mail Menu")
        if e.control.selected_index == 1:
            print("Open Chat Menu")

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
