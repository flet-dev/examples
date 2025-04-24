import flet as ft


def main(page: ft.Page):
    page.title = "Basic elevated buttons"

    page.add(
        ft.ElevatedButton("Elevated button"),
        ft.Button("Disabled button", disabled=True),
    )


ft.run(main)
