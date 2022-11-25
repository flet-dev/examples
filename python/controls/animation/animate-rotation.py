import flet as ft


def main(page: ft.Page):

    c1 = ft.Container(
        width=140,
        height=100,
        left=200,
        top=100,
        bgcolor="red",
        border_radius=5,
        rotate=1,
        animate_rotation=1000,
    )

    c2 = ft.Container(
        width=100,
        height=70,
        bgcolor="blue",
        border_radius=5,
        rotate=ft.transform.Rotate(-1, alignment=ft.alignment.center_left),
        animate_rotation=ft.animation.Animation(duration=300),
    )

    def animate(e):
        c1.rotate += 1
        c2.rotate.angle -= 1
        page.update()

    page.add(
        ft.Stack([c1, c2], width=600, height=600),
        ft.ElevatedButton("Animate!", on_click=animate),
    )


ft.app(target=main)
