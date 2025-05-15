import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK

    def change_theme_mode(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            sw.thumb_icon = ft.Icons.LIGHT_MODE
        else:
            sw.thumb_icon = ft.Icons.DARK_MODE
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    # Yellow page theme with SYSTEM (default) mode
    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.YELLOW,
    )
    sw = ft.Switch(thumb_icon=ft.Icons.DARK_MODE, on_change=change_theme_mode)
    page.add(
        # Page theme
        ft.Row(
            [
                ft.Container(
                    content=ft.ElevatedButton("Page theme button"),
                    bgcolor=ft.Colors.SURFACE_TINT,
                    padding=20,
                    width=300,
                ),
                ft.Container(
                    content=sw,
                    padding=ft.padding.only(bottom=50),
                    alignment=ft.Alignment.top_right(),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        # Inherited theme with primary color overridden
        ft.Container(
            theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.Colors.PINK)),
            content=ft.ElevatedButton("Inherited theme button"),
            bgcolor=ft.Colors.SURFACE_TINT,
            padding=20,
            width=300,
        ),
        # Unique always DARK theme
        ft.Container(
            theme=ft.Theme(color_scheme_seed=ft.Colors.INDIGO),
            theme_mode=ft.ThemeMode.DARK,
            content=ft.ElevatedButton("Unique theme button"),
            bgcolor=ft.Colors.SURFACE_TINT,
            padding=20,
            width=300,
        ),
    )


ft.run(main)
