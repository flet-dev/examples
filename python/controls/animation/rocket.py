from math import pi

import flet as ft


def main(page: ft.Page):

    c2 = ft.Container(
        content=ft.Container(
            ft.Icon(ft.icons.ROCKET, size=40, color="black"),
            scale=1.0,
            animate_scale=1000,
            opacity=1.0,
            animate_opacity=True,
        ),
        width=120,
        height=70,
        alignment=ft.alignment.center_right,
        rotate=ft.transform.Rotate(0, alignment=ft.alignment.center_left),
        animate_rotation=ft.animation.Animation(duration=1000),
    )

    def animate(e):
        c2.rotate.angle -= 0.5 * pi
        c2.content.scale = 2.0 if c2.content.scale == 1.0 else 1.0
        c2.content.opacity = 0.4 if c2.content.scale == 1.0 else 1.0
        page.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Column(
            [
                c2,
                ft.ElevatedButton("Launch!", on_click=animate),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            height=300,
        )
    )


ft.app(target=main)
