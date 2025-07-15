import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(
        ft.CupertinoActivityIndicator(
            radius=50,
            color=ft.Colors.RED,
            animating=True,
        )
    )


ft.run(main)
