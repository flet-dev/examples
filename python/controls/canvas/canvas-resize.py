import flet as ft
import flet.canvas as cv


def main(page: ft.Page):
    def paint_resize(e: cv.CanvasResizeEvent):
        print("On resize:", e.width, e.height)
        cp.shapes[0].x2 = e.width
        cp.shapes[0].y2 = e.height
        cp.shapes[1].y1 = e.height
        cp.shapes[1].x2 = e.width
        cp.update()

    cp = cv.Canvas(
        [
            cv.Line(
                0,
                0,
                100,
                100,
            ),
            cv.Line(
                0,
                100,
                100,
                0,
            ),
        ],
        resize_interval=10,
        on_resize=paint_resize,
    )

    page.add(
        ft.Container(
            cp,
            width=float("inf"),
            expand=True,
        )
    )


ft.app(main)
