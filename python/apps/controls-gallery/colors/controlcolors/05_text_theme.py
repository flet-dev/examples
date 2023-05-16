import flet as ft

name = "Customize Text theme"


def example():
    c = ft.Container(
        theme=ft.Theme(
            text_theme=ft.TextTheme(body_medium=ft.TextStyle(color=ft.colors.GREEN))
        ),
        content=ft.Text("Hello, green world!"),
        height=100,
        width=300,
    )

    return c
