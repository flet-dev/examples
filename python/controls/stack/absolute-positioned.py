import flet
from flet import Column, Container, Page, Stack, colors


def main(page: Page):

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    page.add(
        Container(
            Stack(
                [
                    Container(width=20, height=20, bgcolor=colors.RED, border_radius=5),
                    Container(
                        width=20,
                        height=20,
                        bgcolor=colors.YELLOW,
                        border_radius=5,
                        right=0,
                    ),
                    Container(
                        width=20,
                        height=20,
                        bgcolor=colors.BLUE,
                        border_radius=5,
                        right=0,
                        bottom=0,
                    ),
                    Container(
                        width=20,
                        height=20,
                        bgcolor=colors.GREEN,
                        border_radius=5,
                        left=0,
                        bottom=0,
                    ),
                    Column(
                        [
                            Container(
                                width=20,
                                height=20,
                                bgcolor=colors.PURPLE,
                                border_radius=5,
                            )
                        ],
                        left=35,
                        top=35,
                    ),
                ]
            ),
            border_radius=8,
            padding=5,
            width=100,
            height=100,
            bgcolor=colors.BLACK,
        )
    )


flet.app(target=main)
