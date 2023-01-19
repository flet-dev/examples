import math

import flet
from flet import Container, Page, SweepGradient, alignment


def main(page: Page):

    page.add(
        Container(
            alignment=alignment.center,
            gradient=SweepGradient(
                center=alignment.center,
                start_angle=0.0,
                end_angle=math.pi * 2,
                colors=[
                    "0xFF4285F4",
                    "0xFF34A853",
                    "0xFFFBBC05",
                    "0xFFEA4335",
                    "0xFF4285F4",
                ],
                stops=[0.0, 0.25, 0.5, 0.75, 1.0],
            ),
            width=150,
            height=150,
            border_radius=5,
        )
    )


flet.app(target=main)
