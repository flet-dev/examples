import flet as ft


def main(page: ft.Page):
    page.title = "Text buttons with icons"
    page.add(
        ft.TextButton("Button with icon", icon=ft.Icons.WAVES_OUTLINED),
        ft.TextButton(
            "Button with colorful icon",
            icon=ft.Icons.PARK_ROUNDED,
            icon_color=ft.Colors.GREEN_400,
        ),
    )


ft.run(main)
