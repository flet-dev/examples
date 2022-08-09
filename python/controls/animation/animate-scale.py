import logging

import flet
from flet import (
    ElevatedButton,
    Image,
    Page,
    RadialGradient,
    ShaderMask,
    Stack,
    alignment,
    animation,
    colors,
)


def main(page: Page):

    c1 = ShaderMask(
        Image(
            src="https://picsum.photos/140/100?1",
            width=140,
            height=100,
            fit="fill",
        ),
        blend_mode="colorBurn",
        shader=RadialGradient(
            center=alignment.top_left,
            radius=1.0,
            colors=[colors.YELLOW, colors.DEEP_ORANGE_900],
            tile_mode="clamp",
        ),
        border_radius=5,
        animate_rotation=300,
        animate_scale=animation.Animation(600, "bounceOut"),
    )

    def animate(e):
        c1.rotate = 1
        c1.scale = 3
        page.update()

    page.add(
        Stack([c1], width=600, height=600),
        ElevatedButton("Animate!", on_click=animate),
    )


flet.app(target=main)
