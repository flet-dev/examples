import flet as ft


def main(page: ft.Page):
    page.title = "Basic filled buttons"
    page.add(
        ft.FilledButton(content="Filled button"),
        ft.FilledButton("Disabled button", disabled=True),
        ft.FilledButton("Button with icon", icon=ft.Icons.ADD_OUTLINED),
    )


ft.run(main)
