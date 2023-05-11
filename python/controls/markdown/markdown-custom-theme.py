import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Container(
            content=ft.Markdown(
                "I can read this!",
            ),
            bgcolor="#550000",
            padding=20,
            theme=ft.Theme(
                text_theme=ft.TextTheme(
                    body_medium=ft.TextStyle(color=ft.colors.WHITE),
                    body_large=ft.TextStyle(color=ft.colors.WHITE),
                    body_small=ft.TextStyle(color=ft.colors.WHITE),
                )
            ),
        )
    )


ft.app(target=main)
