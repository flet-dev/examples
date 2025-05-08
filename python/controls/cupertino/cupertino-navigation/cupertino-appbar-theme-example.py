import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    def toggle_theme_mode(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        lightMode.icon = (
            ft.Icons.WB_SUNNY_OUTLINED
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.Icons.WB_SUNNY
        )
        page.update()

    lightMode = ft.IconButton(
        (
            ft.Icons.WB_SUNNY_OUTLINED
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.Icons.WB_SUNNY
        ),
        on_click=toggle_theme_mode,
    )
    page.appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.Icons.PALETTE),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        trailing=lightMode,
        middle=ft.Text("CupertinoAppBar Example"),
    )
    page.add(ft.Text("Body!"))


ft.run(main)
