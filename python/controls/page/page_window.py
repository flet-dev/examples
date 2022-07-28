import flet
from flet import (
    Column,
    Container,
    ElevatedButton,
    IconButton,
    Page,
    Row,
    Switch,
    Text,
    alignment,
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

    def maximize_clicked(e):
        page.window_maximized = True
        page.update()

    def minimize_clicked(e):
        page.window_minimized = True
        page.update()

    def full_screen_changed(e):
        page.window_full_screen = full_screen.value
        maximize.disabled = full_screen.value
        minimize.disabled = full_screen.value
        page.update()

    def resizable_changed(e):
        page.window_resizable = resizable.value
        maximize.disabled = not resizable.value
        minimize.disabled = not resizable.value
        page.update()

    always_on_top = Switch(value=False, on_change=always_on_top_changed)

    full_screen = Switch(
        label="Full screen", value=False, on_change=full_screen_changed
    )

    resizable = Switch(label="Resizable", value=True, on_change=resizable_changed)

    maximize = ElevatedButton(text="Maximize", on_click=maximize_clicked)
    minimize = ElevatedButton(text="Minimize", on_click=minimize_clicked)

    def update_coordinates():
        top.value = f"Top: {page.window_top}"
        left.value = f"Left: {page.window_left}"

    def window_changed(e):
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
        Row(
            controls=[
                Container(
                    expand=1,
                    bgcolor=colors.LIGHT_BLUE_500,
                    alignment=alignment.center,
                    content=always_on_top,
                ),
                Container(expand=1, alignment=alignment.center, content=maximize),
                Container(expand=1, alignment=alignment.center, content=full_screen),
            ],
        ),
        Row(
            alignment="spaceBetween",
            controls=[
                Column(expand=1, controls=[Text()]),
                Column(
                    expand=1,
                    controls=[
                        Container(
                            bgcolor=colors.AMBER_200,
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
                                                    icon=icons.KEYBOARD_ARROW_UP,
                                                    on_click=move_up,
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
                                                    icon=icons.KEYBOARD_ARROW_LEFT,
                                                    on_click=move_left,
                                                ),
                                            ),
                                            Container(
                                                bgcolor=colors.LIGHT_BLUE_500,
                                                border_radius=border_radius.all(30),
                                                content=IconButton(
                                                    icon=icons.KEYBOARD_ARROW_RIGHT,
                                                    on_click=move_right,
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
                                                    icon=icons.KEYBOARD_ARROW_DOWN,
                                                    on_click=move_down,
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        )
                    ],
                ),
                Column(expand=1, controls=[resizable]),
            ],
        ),
        Row(
            # alignment="spaceBetween",
            controls=[
                Container(
                    expand=1,
                    alignment=alignment.center,
                    bgcolor=colors.AMBER_100,
                    content=Column(
                        controls=[
                            Row(controls=[top]),
                            Row(controls=[left]),
                            Row(controls=[width]),
                            Row(controls=[height]),
                        ],
                    ),
                ),
                Container(
                    expand=1,
                    bgcolor=colors.AMBER_200,
                    content=minimize,
                    alignment=alignment.center,
                ),
                Container(expand=1, bgcolor=colors.AMBER_300, content=Text()),
            ],
        ),
    )


flet.app(target=main)
