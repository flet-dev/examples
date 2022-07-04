import flet
from flet import (
    Column,
    Container,
    IconButton,
    Page,
    Row,
    Switch,
    Text,
    border,
    border_radius,
    colors,
    icons,
    padding,
)


def main(page: Page):
    # set page properties
    page.horizontal_alignment = "center"
    page.vertical_alignment = "spaceBetween"

    top = Text(f"Top: {page.window_top}")
    left = Text(f"Left: {page.window_left}")
    width = Text(f"Width: {page.width}")
    height = Text(f"Height: {page.height}")

    def always_on_top_changed(e):
        page.window_always_on_top = always_on_top.value
        page.update()

    always_on_top = Switch(
        label="Always on top", value=False, on_change=always_on_top_changed
    )

    def update_coordinates():
        top.value = f"Top: {page.window_top}"
        left.value = f"Left: {page.window_left}"

    def window_changed(e):
        print("window changed!")
        update_coordinates()
        width.value = f"Width: {page.width}"
        height.value = f"Height: {page.height}"
        page.update()

    def move_up(e):
        page.window_top = page.window_top - 10
        update_coordinates()
        page.update()

    def move_down(e):
        page.window_top = page.window_top + 10
        update_coordinates()
        page.update()

    def move_left(e):
        page.window_left = page.window_left - 10
        update_coordinates()
        page.update()

    def move_right(e):
        page.window_left = page.window_left + 10
        update_coordinates()
        page.update()

    page.on_window_event = window_changed

    # add controls on Page
    page.add(
        Column(controls=[always_on_top]),
        Container(
            width=300,
            height=300,
            border=border.all(1, colors.BLACK),
            padding=padding.all(10),
            content=Column(
                alignment="spaceBetween",
                controls=[
                    Row(
                        alignment="center",
                        controls=[
                            Container(
                                bgcolor=colors.LIGHT_BLUE_500,
                                border_radius=border_radius.all(30),
                                content=IconButton(
                                    icon=icons.KEYBOARD_ARROW_UP, on_click=move_up
                                ),
                            ),
                        ],
                    ),
                    Row(
                        alignment="spaceBetween",
                        controls=[
                            Container(
                                bgcolor=colors.LIGHT_BLUE_500,
                                border_radius=border_radius.all(30),
                                content=IconButton(
                                    icon=icons.KEYBOARD_ARROW_LEFT, on_click=move_left
                                ),
                            ),
                            Container(
                                bgcolor=colors.LIGHT_BLUE_500,
                                border_radius=border_radius.all(30),
                                content=IconButton(
                                    icon=icons.KEYBOARD_ARROW_RIGHT, on_click=move_right
                                ),
                            ),
                        ],
                    ),
                    Row(
                        alignment="center",
                        controls=[
                            Container(
                                bgcolor=colors.LIGHT_BLUE_500,
                                border_radius=border_radius.all(30),
                                content=IconButton(
                                    icon=icons.KEYBOARD_ARROW_DOWN, on_click=move_down
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        ),
        Column(
            controls=[
                Row(alignment="start", controls=[top]),
                Row(alignment="start", controls=[left]),
                Row(alignment="start", controls=[width]),
                Row(alignment="start", controls=[height]),
            ]
        ),
    )


flet.app(target=main)
