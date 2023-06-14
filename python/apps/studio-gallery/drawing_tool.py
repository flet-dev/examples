import flet as ft
import flet.canvas as cv


def example():
    class State:
        x: float
        y: float

    state = State()
    state.color = "black"

    colors = [
        "red",
        "yellow",
        "blue",
        "green",
        "orange",
        "purple",
        "pink",
        "lime",
        "black",
    ]

    color_buttons = []

    def color_changed(e):
        state.color = e.control.bgcolor
        for color_button in color_buttons:
            color_button.border = None
            color_button.update()
        e.control.border = ft.border.all(2)
        e.control.update()

    for color in colors:
        color_buttons.append(
            ft.Container(
                width=30,
                height=30,
                border_radius=30,
                bgcolor=color,
                on_click=color_changed,
            )
        )

    def pan_start(e: ft.DragStartEvent):
        state.x = e.local_x
        state.y = e.local_y

    def pan_update(e: ft.DragUpdateEvent):
        cp.shapes.append(
            cv.Line(
                state.x,
                state.y,
                e.local_x,
                e.local_y,
                paint=ft.Paint(stroke_width=3, color=state.color),
            )
        )
        cp.update()
        state.x = e.local_x
        state.y = e.local_y

    cp = cv.Canvas(
        [
            cv.Fill(
                ft.Paint(
                    gradient=ft.PaintLinearGradient(
                        (0, 0), (600, 600), colors=[ft.colors.CYAN_50, ft.colors.GREY]
                    )
                )
            ),
        ],
        content=ft.GestureDetector(
            on_pan_start=pan_start,
            on_pan_update=pan_update,
            drag_interval=10,
        ),
        expand=False,
    )

    return ft.Column(
        expand=True,
        controls=[
            ft.Row(
                controls=color_buttons, alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Container(cp, border_radius=5, expand=True),
        ],
    )


def main(page: ft.Page):
    page.title = "Free-hand drawing tool"
    page.window_width = 390
    page.window_height = 844
    page.add(example())


if __name__ == "__main__":
    ft.app(target=main)
