import flet as ft

name = "Basic ElevatedButtons"


def example():
    return ft.Column(
        controls=[
            ft.ElevatedButton(text="Elevated button"),
            ft.ElevatedButton("Disabled button", disabled=True),
        ]
    )
