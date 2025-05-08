import flet as ft
from flet import Container, ElevatedButton, Page, Row, colors, padding


def main(page: ft.Page):
    page.title = "Containers with different padding"

    c1 = ft.Container(
        content=ft.ElevatedButton("container_1"),
        bgcolor=ft.Colors.AMBER,
        padding=ft.Padding.all(10),
        width=150,
        height=150,
    )

    c2 = ft.Container(
        content=ft.ElevatedButton("container_2"),
        bgcolor=ft.Colors.AMBER,
        padding=ft.Padding.all(20),
        width=150,
        height=150,
    )

    c3 = ft.Container(
        content=ft.ElevatedButton("container_3"),
        bgcolor=ft.Colors.AMBER,
        padding=ft.padding.symmetric(horizontal=10),
        width=150,
        height=150,
    )

    c4 = ft.Container(
        content=ft.ElevatedButton("container_4"),
        bgcolor=ft.Colors.AMBER,
        padding=ft.padding.only(left=10),
        width=150,
        height=150,
    )

    r = ft.Row([c1, c2, c3, c4])
    page.add(r)


ft.run(main)
