import flet as ft


def main(page: ft.Page):
    page.title = "Containers with different margins"

    c1 = ft.Container(
        content=ft.ElevatedButton("container_1"),
        bgcolor=ft.Colors.AMBER,
        # padding=ft.Padding.all(10),
        margin=ft.Margin.all(10),
        width=200,
        height=200,
    )

    c2 = ft.Container(
        content=ft.ElevatedButton("container_2"),
        bgcolor=ft.Colors.AMBER,
        # padding=ft.Padding.all(20),
        margin=ft.Margin.all(20),
        width=200,
        height=200,
    )

    c3 = ft.Container(
        content=ft.ElevatedButton("container_3"),
        bgcolor=ft.Colors.AMBER,
        # padding=ft.padding.symmetric(horizontal=10),
        margin=ft.Margin.symmetric(vertical=10),
        width=200,
        height=200,
    )

    c4 = ft.Container(
        content=ft.ElevatedButton("container_4"),
        bgcolor=ft.Colors.AMBER,
        # padding=ft.padding.only(left=10),
        margin=ft.Margin.only(left=10),
        width=200,
        height=200,
    )

    r = ft.Row([c1, c2, c3, c4], spacing=0)
    page.add(r)


ft.run(main)
