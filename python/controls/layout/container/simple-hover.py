import flet as ft


def main(page: ft.Page):
    def on_hover(e):
        print(e)
        c.bgcolor = ft.Colors.BLUE if e.data else ft.Colors.RED
        c.update()

    c = ft.Container(
        width=200, height=200, bgcolor=ft.Colors.RED, ink=False, on_hover=on_hover
    )
    page.add(c)


ft.run(main)
