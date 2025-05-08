import flet as ft


def main(page: ft.Page):
    page.title = "Containers with different background color"

    c1 = ft.Container(
        content=ft.Text("Container_1"),
        bgcolor="#FFCC0000",
        padding=5,
    )

    c2 = ft.Container(
        content=ft.Text("Container_2"),
        bgcolor="#CC0000",
        padding=5,
    )

    c3 = ft.Container(
        content=ft.Text("Container_3"),
        bgcolor=ft.Colors.RED,
        padding=5,
    )
    page.add(c1, c2, c3)


ft.run(main)
