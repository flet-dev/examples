import flet
from flet import Container, IconButton, Page, Row, Text, WindowDragArea, colors, icons


def main(page: Page):
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True

    page.add(
        Row(
            [
                WindowDragArea(Container(Text("Drag this area to move, maximize and restore application window."), bgcolor=colors.AMBER_300, padding=10), expand=True),
                IconButton(icons.CLOSE, on_click=lambda _: page.window_close())
            ]
        )
    )


flet.app(target=main)
