import flet as ft


def main(page: ft.Page):
    page.title = "Elevated buttons with icons"

    page.add(
        ft.ElevatedButton("Button with icon", icon=ft.Icons.WAVES_ROUNDED),
        ft.ElevatedButton(
            "Button with colorful icon",
            icon=ft.Icons.PARK_ROUNDED,
            icon_color=ft.Colors.GREEN_400,
        ),
    )


ft.run(main)
