import flet as ft


def main(page: ft.Page):
    page.title = "Basic text buttons"
    page.add(
        ft.TextButton(content="Text button"),
        ft.TextButton("Disabled button", disabled=True),
    )


ft.app(main)
