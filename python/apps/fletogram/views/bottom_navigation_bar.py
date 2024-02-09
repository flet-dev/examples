import flet as ft


class BottomNavigationBar(ft.NavigationBar):
    def __init__(self, tabs):
        super().__init__()
        self.tabs = tabs
        self.selected_index = 1
        self.destinations = [
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
        ]
        self.on_change = self.destination_changed
        for tab in tabs:
            tab.navigation_bar = self

    def destination_changed(self, e):
        self.page.views.clear()
        self.page.views.append(self.tabs[self.selected_index])
        self.page.update()
