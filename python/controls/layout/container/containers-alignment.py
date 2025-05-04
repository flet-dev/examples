import flet as ft


def main(page: ft.Page):
    page.title = "Containers with different alignments"

    c1 = ft.Container(
        content=ft.ElevatedButton("Center"),
        bgcolor=ft.Colors.AMBER,
        padding=15,
        alignment=ft.Alignment.center(),
        width=150,
        height=150,
    )

    c2 = ft.Container(
        content=ft.ElevatedButton("Top left"),
        bgcolor=ft.Colors.AMBER,
        padding=15,
        alignment=ft.alignment.top_left,
        width=150,
        height=150,
    )

    c3 = ft.Container(
        content=ft.ElevatedButton("-0.5, -0.5"),
        bgcolor=ft.Colors.AMBER,
        padding=15,
        alignment=ft.alignment.Alignment(-0.5, -0.5),
        width=150,
        height=150,
    )

    r = ft.Row([c1, c2, c3])
    page.add(r)


ft.app(main)
