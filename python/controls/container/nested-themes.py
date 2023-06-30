import flet as ft


def main(page: ft.Page):
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.YELLOW,
        color_scheme=ft.ColorScheme(
            primary=ft.colors.GREEN, primary_container=ft.colors.GREEN_200
        ),
    )

    page.add(
        ft.Row(
            [
                ft.ElevatedButton("Page theme"),
                ft.TextButton("Page theme text button"),
                ft.Text(
                    "Text in primary container color",
                    color=ft.colors.PRIMARY_CONTAINER,
                ),
            ]
        ),
        ft.Container(
            content=ft.Row(
                [
                    ft.ElevatedButton("Inherited theme with primary color overriden"),
                    ft.TextButton("Button 2"),
                ]
            ),
            height=100,
            theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.PINK)),
        ),
        ft.Container(
            content=ft.Row(
                [
                    ft.ElevatedButton("Always DARK theme"),
                    ft.TextButton("Text button"),
                    ft.Text(
                        "Text in primary container color",
                        color=ft.colors.PRIMARY_CONTAINER,
                    ),
                ]
            ),
            padding=20,
            bgcolor=ft.colors.BACKGROUND,
            theme_mode=ft.ThemeMode.DARK,
            theme=ft.Theme(
                color_scheme_seed=ft.colors.GREEN,
                color_scheme=ft.ColorScheme(primary_container=ft.colors.BLUE),
            ),
        ),
        ft.Container(
            content=ft.Row(
                [
                    ft.ElevatedButton("Always LIGHT theme"),
                    ft.TextButton("Text button"),
                    ft.Text(
                        "Text in primary container color",
                        color=ft.colors.PRIMARY_CONTAINER,
                    ),
                ]
            ),
            padding=20,
            bgcolor=ft.colors.SURFACE_VARIANT,
            border=ft.border.all(3, ft.colors.OUTLINE),
            theme_mode=ft.ThemeMode.LIGHT,
            theme=ft.Theme(),
        ),
        ft.Container(
            content=ft.Row(
                [
                    ft.ElevatedButton("SYSTEM theme"),
                    ft.TextButton("Text button"),
                    ft.Text(
                        "Text in primary container color",
                        color=ft.colors.PRIMARY_CONTAINER,
                    ),
                ]
            ),
            padding=20,
            bgcolor=ft.colors.SURFACE,
            border=ft.border.all(3, ft.colors.OUTLINE),
            border_radius=10,
            theme_mode=ft.ThemeMode.SYSTEM,
            theme=ft.Theme(),
        ),
    )


ft.app(main)
