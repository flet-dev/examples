import flet as ft


def main(page: ft.Page):
    page.title = "Basic outlined buttons"
    page.add(
        ft.OutlinedButton(text="Outlined button"),
        ft.OutlinedButton("Disabled button", disabled=True),
    )


ft.app(main)
