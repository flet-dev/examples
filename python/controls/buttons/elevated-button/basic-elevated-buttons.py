import flet as ft


def main(page: ft.Page):
    page.title = "Basic elevated buttons"

    page.add(
        ft.ElevatedButton(text="Elevated button"),
        ft.Button("Disabled button", disabled=True),
    )


ft.app(main)
