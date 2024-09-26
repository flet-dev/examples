import flet as ft

name = "Placeholder example"


def example():
    return ft.Placeholder(
        expand=True, color=ft.colors.random_color()  # random material color
    )
