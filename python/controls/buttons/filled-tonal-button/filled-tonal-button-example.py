import flet as ft


def main(page: ft.Page):
    page.title = "Basic filled tonal buttons"

    page.add(
        ft.FilledTonalButton(content="Filled tonal button"),
        ft.FilledTonalButton(content="Disabled button", disabled=True),
        ft.FilledTonalButton(content="Button with icon", icon=ft.Icons.ADD_OUTLINED),
    )


ft.run(main)
