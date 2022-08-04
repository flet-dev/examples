import flet
from flet import Alignment, Container, Page, RadialGradient, alignment


def main(page: Page):

    page.add(
        Container(
            alignment=alignment.center,
            gradient=RadialGradient(
                center=Alignment(0.7, -0.6),
                radius=0.2,
                colors=[
                    "0xFFFFFF00",  # yellow sun
                    "0xFF0099FF",  # blue sky
                ],
                stops=[0.4, 1.0],
            ),
            width=150,
            height=150,
            border_radius=5,
        )
    )


flet.app(target=main)
