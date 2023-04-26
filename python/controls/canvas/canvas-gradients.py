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
                        (0, 10), (0, 100), colors=[ft.colors.BLUE, ft.colors.YELLOW]
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
                [
                    cv.Path.MoveTo(60, 230),
                    cv.Path.LineTo(110, 330),
                    cv.Path.LineTo(10, 330),
                    cv.Path.Close(),
                ],
                ft.Paint(
                    gradient=ft.PaintSweepGradient(
                        (60, 280),
                        colors=[ft.colors.YELLOW, ft.colors.BLUE],
                        start_angle=0,
                        end_angle=math.pi * 2,
                    ),
                    stroke_width=5,
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
