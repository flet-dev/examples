import flet as ft


class ContactsView(ft.View):
    def __init__(self, fletogram):
        super().__init__()
        self.route = ("/",)
        self.appbar = ft.AppBar(  # adaptive=True,
            leading=ft.TextButton("Edit"),
            title=ft.Text("Contacts"),
            actions=[
                ft.IconButton(icon=ft.icons.ADD_CARD),
            ],
        )
        self.fletogram = fletogram
        self.controls = [ft.ListView(spacing=5, controls=self.fletogram.users)]

        self.navigation_bar = self.fletogram.navigation_bar
