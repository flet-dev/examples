import flet as ft


def main(page: ft.Page):
    page.title = "Elevated buttons with icons"

    page.add(
        ft.ElevatedButton("Button with icon", icon="chair_outlined"),
        ft.ElevatedButton(
            "Button with colorful icon",
            icon="park_rounded",
            icon_color=ft.Colors.GREEN_400,
        ),
    )


ft.app(main)
