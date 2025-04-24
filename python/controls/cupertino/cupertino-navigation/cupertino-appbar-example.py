import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    page.appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.Icons.PALETTE),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        trailing=ft.Icon(ft.Icons.WB_SUNNY_OUTLINED),
        middle=ft.Text("CupertinoAppBar Example"),
        brightness=ft.Brightness.LIGHT,
    )
    page.add(ft.Text("Body!"))


ft.app(main)
