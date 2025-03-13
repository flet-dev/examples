import flet as ft


def main(page: ft.Page):
    page.title = "Outlined buttons with icons"
    page.add(
        ft.OutlinedButton("Button with icon", icon="chair_outlined"),
        ft.OutlinedButton(
            "Button with colorful icon",
            icon="park_rounded",
            icon_color="green400",
        ),
    )


ft.app(main)
