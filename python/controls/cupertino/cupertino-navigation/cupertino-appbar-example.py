import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    page.appbar = ft.CupertinoAppBar(
        automatic_background_visibility=False,
        leading=ft.Icon(ft.Icons.PALETTE, color=ft.Colors.ON_SECONDARY),
        bgcolor=ft.Colors.SECONDARY,
        trailing=ft.Icon(ft.Icons.WB_SUNNY_OUTLINED, color=ft.Colors.ON_SECONDARY),
        middle=ft.Text("CupertinoAppBar Example"),
        brightness=ft.Brightness.LIGHT,
    )
    page.add(ft.Text("Body!"))


ft.run(main)
