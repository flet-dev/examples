import flet
from flet import Container, IconButton, Page, Row, Text, WindowDragArea, colors, icons

def main(page: Page):
    # Use the updated properties for window title bar settings
    page.window.title_bar_hidden = True
    page.window.title_bar_buttons_hidden = True

    page.add(
        Row(
            [
                WindowDragArea(
                    Container(
                        Text(
                            "Drag this area to move, maximize and restore application window."
                        ),
                        bgcolor=colors.AMBER_300,
                        padding=10,
                    ),
                    expand=True,
                ),
                # Use the updated method to close the window
                IconButton(icons.CLOSE, on_click=lambda _: page.window.close()),
            ]
        )
    )

flet.app(target=main)

