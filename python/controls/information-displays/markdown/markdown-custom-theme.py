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

    sw = ft.Switch(thumb_icon=ft.Icons.DARK_MODE, on_change=change_theme_mode)

    page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.Markdown(
                        "I can read this!",
                    ),
                    bgcolor="#550000",
                    padding=20,
                    theme=ft.Theme(
                        text_theme=ft.TextTheme(
                            body_medium=ft.TextStyle(color=ft.Colors.WHITE),
                            body_large=ft.TextStyle(color=ft.Colors.WHITE),
                            body_small=ft.TextStyle(color=ft.Colors.WHITE),
                        )
                    ),
                ),
                ft.Container(
                    content=sw,
                    padding=ft.padding.only(bottom=50),
                    alignment=ft.Alignment.top_right(),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
    )


ft.run(main)
