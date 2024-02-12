import flet as ft


class SettingsView(ft.View):
    def __init__(self, fletogram):
        super().__init__()
        self.route = "/"
        self.appbar = ft.AppBar(
            title=ft.Text("Settings"),
        )
        self.fletogram = fletogram
        self.controls = [ft.Text("Settings")]

        self.navigation_bar = self.fletogram.navigation_bar
