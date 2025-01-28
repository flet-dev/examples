import logging
import flet
from flet import ElevatedButton, SnackBar, Text

logging.basicConfig(level=logging.DEBUG)


class Data:
    def __init__(self) -> None:
        self.counter = 0


d = Data()


def main(page):

    snack_bar = SnackBar(
        content=Text("Hello, world!"),
        action="Alright!"
    )

    def on_click(e):
        d.counter += 1
        snack_bar.content = Text(f"Hello {d.counter}")
        snack_bar.open = True
        
        page.add(snack_bar)
        page.update()

    page.add(ElevatedButton("Open SnackBar", on_click=on_click))

    page.add(snack_bar)


flet.app(target=main)
