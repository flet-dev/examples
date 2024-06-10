import flet as ft


class MobileLayout(ft.View):
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

        self.drawer = ft.NavigationDrawer(
            controls=[ft.Text("Inbox"), ft.Text("Starred")]
        )
        self.appbar = ft.AppBar(leading=self.open_menu_button)

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
