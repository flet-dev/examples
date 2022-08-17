from math import pi

import flet
from flet import (
    Column,
    Container,
    ElevatedButton,
    Icon,
    Page,
    alignment,
    animation,
    icons,
    transform,
)


def main(page: Page):

    c2 = Container(
        content=Container(
            Icon(icons.ROCKET, size=40, color="black"),
            scale=1.0,
            animate_scale=1000,
            opacity=1.0,
            animate_opacity=True,
        ),
        width=120,
        height=70,
        alignment=alignment.center_right,
        rotate=transform.Rotate(0, alignment=alignment.center_left),
        animate_rotation=animation.Animation(duration=1000),
    )

    def animate(e):
        c2.rotate.angle -= 0.5 * pi
        c2.content.scale = 2.0 if c2.content.scale == 1.0 else 1.0
        c2.content.opacity = 0.4 if c2.content.scale == 1.0 else 1.0
        page.update()

    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    page.add(
        Column(
            [
                c2,
                ElevatedButton("Launch!", on_click=animate),
            ],
            alignment="spaceBetween",
            height=300,
        )
    )


flet.app(target=main)
