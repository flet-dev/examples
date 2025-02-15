import math

import flet
from flet import Alignment, Container, LinearGradient, Page, alignment


def main(page: Page):

    page.add(
        Container(
            alignment=alignment.center,
            gradient=LinearGradient(
                begin=alignment.top_left,
                end=Alignment(0.8, 1),
                colors=[
                    "0xff1f005c",
                    "0xff5b0060",
                    "0xff870160",
                    "0xffac255e",
                    "0xffca485c",
                    "0xffe16b5c",
                    "0xfff39060",
                    "0xffffb56b",
                ],
                tile_mode="mirror",
                rotation=math.pi / 3,
            ),
            width=150,
            height=150,
            border_radius=5,
        )
    )


flet.app(target=main)
