import flet as ft


class MessageView(ft.View):
    def __init__(self, message):
        super().__init__()
        self.appbar = ft.AppBar(title=ft.Text(f"{message.title}"))
        self.controls = [ft.Text(f"{message.body}")]
