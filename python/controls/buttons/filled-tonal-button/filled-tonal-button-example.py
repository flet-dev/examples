import flet as ft


def main(page: ft.Page):
    page.title = "Basic filled tonal buttons"
    page.add(
        ft.FilledTonalButton(text="Filled tonal button"),
        ft.FilledTonalButton("Disabled button", disabled=True),
        ft.FilledTonalButton("Button with icon", icon=ft.Icons.ADD_OUTLINED),
    )


ft.app(main)
