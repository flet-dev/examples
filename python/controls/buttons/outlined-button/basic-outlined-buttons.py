import flet as ft


def main(page: ft.Page):
    page.title = "Basic outlined buttons"
    page.add(
        ft.OutlinedButton(content="Outlined button"),
        ft.OutlinedButton("Disabled button", disabled=True),
    )


ft.run(main)
