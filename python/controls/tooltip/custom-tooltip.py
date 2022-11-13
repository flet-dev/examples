import math

import flet as ft
from flet import alignment


def main(page: ft.Page):
    page.title = "Tooltip Example"
    page.add(
        ft.Tooltip(
            message="This is tooltip",
            content=ft.Text("Hover to see tooltip"),
            padding=20,
            border_radius=10,
            text_style=ft.TextStyle(size=20, color=ft.colors.WHITE),
            gradient=ft.LinearGradient(
                begin=alignment.top_left,
                end=alignment.Alignment(0.8, 1),
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
        )
    )


ft.app(target=main)
