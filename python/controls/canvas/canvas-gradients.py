import math

import flet as ft
import flet.canvas as cv


def main(page: ft.Page):
    cp = cv.Canvas(
        [
            cv.Rect(
                10,
                10,
                100,
                100,
                5,
                ft.Paint(
                    gradient=ft.PaintLinearGradient(
                        (0, 10),
                        (100, 50),
                        colors=[ft.colors.BLUE, ft.colors.YELLOW],
                        # rotation=math.pi / 2,
                    ),
                    style=ft.PaintingStyle.FILL,
                ),
            ),
            cv.Circle(
                60,
                170,
                50,
                ft.Paint(
                    gradient=ft.PaintRadialGradient(
                        (60, 170), 50, colors=[ft.colors.YELLOW, ft.colors.BLUE]
                    ),
                    style=ft.PaintingStyle.FILL,
                ),
            ),
            cv.Path(
                [cv.Path.Arc(10, 230, 100, 100, 3 * math.pi / 4, 3 * math.pi / 2)],
                ft.Paint(
                    gradient=ft.PaintSweepGradient(
                        (60, 280),
                        colors=[ft.colors.YELLOW, ft.colors.PURPLE],
                        color_stops=[0.0, 1.0],
                        start_angle=0,
                        end_angle=math.pi * 2,
                        rotation=3 * math.pi / 4,
                    ),
                    stroke_width=15,
                    stroke_join=ft.StrokeJoin.ROUND,
                    style=ft.PaintingStyle.STROKE,
                ),
            ),
        ],
        width=float("inf"),
        expand=True,
    )

    page.add(cp)


ft.app(main)
