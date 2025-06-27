import flet as ft


def main(page: ft.Page):
    page.title = "Basic elevated buttons"

    page.add(
        ft.ElevatedButton(content="Elevated button"),
        ft.Button(content="Disabled button", disabled=True),
    )


ft.run(main)
