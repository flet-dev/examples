import math

import flet
from flet import (
    Alignment,
    Container,
    LinearGradient,
    Page,
    Row,
    Text,
    alignment,
    colors,
)
from flet.gradients import RadialGradient, SweepGradient


def main(page: Page):
    page.title = "Containers with gradient"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    page.add(
        Row(
            [
                Container(
                    content=Text("Linear gradient"),
                    padding=10,
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
                    width=200,
                    height=200,
                    border_radius=10,
                ),
                Container(
                    content=Text("Linear gradient with stops"),
                    padding=10,
                    alignment=alignment.center,
                    gradient=LinearGradient(
                        begin=alignment.center_left,
                        end=alignment.center_right,
                        colors=[colors.RED, colors.GREEN, colors.BLUE],
                        stops=[0.1, 0.2, 1.0],
                        tile_mode="mirror",
                    ),
                    width=200,
                    height=200,
                    border_radius=10,
                ),
                Container(
                    content=Text("Radial gradient"),
                    padding=10,
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
                    width=200,
                    height=200,
                    border_radius=10,
                ),
                Container(
                    content=Text("Sweep gradient"),
                    padding=10,
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
                        rotation=math.pi / 4,
                    ),
                    width=200,
                    height=200,
                    border_radius=10,
                ),
            ],
            alignment="center",
        ),
    )


flet.app(target=main)
