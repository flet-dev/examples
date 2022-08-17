import logging

import flet
from flet import Column, ElevatedButton, Image, Page, animation


def main(page: Page):

    c = Image(
        src="icons/icon-192.png",
        width=100,
        height=100,
        scale=1.0,
        animate_scale=animation.Animation(300, "easeInQuint"),
        opacity=1.0,
        animate_opacity=animation.Animation(300, "easeInQuint"),
    )

    def animate(e):
        c.scale = 30
        c.opacity = 0
        c.update()

    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(
        Column(
            [c, ElevatedButton("Boom!", on_click=animate)],
            horizontal_alignment="center",
        )
    )


flet.app(target=main)
