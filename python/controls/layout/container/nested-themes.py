import flet as ft


def main(page: ft.Page):
    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.YELLOW,
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.GREEN, primary_container=ft.Colors.GREEN_200
        ),
    )

    page.add(
        ft.Row(
            [
                ft.ElevatedButton("Page theme"),
                ft.TextButton("Page theme text button"),
                ft.Text(
                    "Text in primary container color",
                    color=ft.Colors.PRIMARY_CONTAINER,
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
            theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.Colors.PINK)),
        ),
        ft.Container(
            content=ft.Row(
                [
                    ft.ElevatedButton("Always DARK theme"),
                    ft.TextButton("Text button"),
                    ft.Text(
                        "Text in primary container color",
                        color=ft.Colors.PRIMARY_CONTAINER,
                    ),
                ]
            ),
            padding=20,
            bgcolor=ft.Colors.SURFACE,
            theme_mode=ft.ThemeMode.DARK,
            theme=ft.Theme(
                color_scheme_seed=ft.Colors.GREEN,
                color_scheme=ft.ColorScheme(primary_container=ft.Colors.BLUE),
            ),
        ),
        ft.Container(
            content=ft.Row(
                [
                    ft.ElevatedButton("Always LIGHT theme"),
                    ft.TextButton("Text button"),
                    ft.Text(
                        "Text in primary container color",
                        color=ft.Colors.PRIMARY_CONTAINER,
                    ),
                ]
            ),
            padding=20,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            border=ft.border.all(3, ft.Colors.OUTLINE),
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
                        color=ft.Colors.PRIMARY_CONTAINER,
                    ),
                ]
            ),
            padding=20,
            bgcolor=ft.Colors.SURFACE,
            border=ft.border.all(3, ft.Colors.OUTLINE),
            border_radius=10,
            theme_mode=ft.ThemeMode.SYSTEM,
            theme=ft.Theme(),
        ),
    )


ft.run(main)
