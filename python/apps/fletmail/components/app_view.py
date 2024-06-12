import flet as ft


class AppView(ft.View):
    def __init__(self):
        super().__init__(route="/")

    def display_inbox(self): ...

    def display_chat(self): ...

    def display_meet(self): ...

    def display_message(self): ...
