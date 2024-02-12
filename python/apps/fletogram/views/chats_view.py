import flet as ft


class ChatView(ft.View):
    def __init__(self, fletogram):
        super().__init__()
        self.route = "/"
        self.appbar = ft.AppBar(
            leading=ft.TextButton("Edit"),
            title=ft.Text("Chats"),
            actions=[
                ft.IconButton(icon=ft.icons.ADD_COMMENT),
            ],
        )
        self.fletogram = fletogram
        self.controls = [
            ft.ListView(
                spacing=0,
                controls=self.fletogram.chats,
            )
        ]

        self.navigation_bar = self.fletogram.navigation_bar
