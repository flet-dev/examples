import flet as ft


def main(page: ft.Page):

    c = ft.Container(
        width=150,
        height=150,
        bgcolor=ft.Colors.RED,
        animate=ft.animation.Animation(1000, ft.AnimationCurve.BOUNCE_OUT),
    )

    def animate_container(e):
        c.width = 100 if c.width == 150 else 150
        c.height = 50 if c.height == 150 else 150
        c.bgcolor = ft.Colors.BLUE if c.bgcolor == ft.Colors.RED else ft.Colors.RED
        c.update()

    page.add(c, ft.ElevatedButton("Animate container", on_click=animate_container))


ft.app(main)
