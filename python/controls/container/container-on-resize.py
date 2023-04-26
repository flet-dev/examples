import flet as ft
import flet.canvas as cv


class SizeAwareContainer(cv.Canvas):
    def __init__(self, color, expand):
        super().__init__(expand=expand)
        self.size = ft.Text()
        self.content = ft.Container(
            self.size,
            alignment=ft.alignment.center,
            bgcolor=color,
        )
        self.resize_interval = 100
        self.on_resize = self.canvas_resize

    def canvas_resize(self, e):
        self.size.value = f"{int(e.width)} x {int(e.height)}"
        self.update()


def main(page: ft.Page):
    page.add(
        ft.Row(
            [
                SizeAwareContainer(ft.colors.RED, expand=2),
                SizeAwareContainer(ft.colors.GREEN, expand=4),
            ],
            expand=2,
        ),
        ft.Row(
            [
                SizeAwareContainer(ft.colors.YELLOW, expand=2),
                SizeAwareContainer(ft.colors.BLUE, expand=4),
            ],
            expand=3,
        ),
    )


ft.app(main)
