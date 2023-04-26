import math

import flet as ft
import flet.canvas as cv


def main(page: ft.Page):
    cp = cv.Canvas(
        [
            cv.Path(
                [
                    cv.Path.MoveTo(25, 25),
                    cv.Path.LineTo(105, 25),
                    cv.Path.LineTo(25, 105),
                ],
                paint=ft.Paint(
                    style=ft.PaintingStyle.FILL,
                ),
            ),
            cv.Path(
                [
                    cv.Path.MoveTo(125, 125),
                    cv.Path.LineTo(125, 45),
                    cv.Path.LineTo(45, 125),
                    cv.Path.Close(),
                ],
                paint=ft.Paint(
                    stroke_width=2,
                    style=ft.PaintingStyle.STROKE,
                ),
            ),
        ],
        width=float("inf"),
        expand=True,
    )

    page.add(cp)


ft.app(main)
