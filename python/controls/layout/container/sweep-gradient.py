import math
import flet as ft


def main(page: ft.Page):

    page.add(
        ft.Container(
            alignment=ft.alignment.center,
            gradient=ft.SweepGradient(
                center=ft.alignment.center,
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


ft.app(main)
