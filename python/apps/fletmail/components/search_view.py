import flet as ft


class SearchView(ft.View):
    def __init__(self):
        super().__init__()
        self.appbar = ft.AppBar(title=ft.TextField(f"Search in mail"))
        self.controls = [ft.Text(f"RECENT MAIL SEARCHES")]
