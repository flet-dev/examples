import logging
import flet as ft


logging.basicConfig(level=logging.DEBUG)


class Data:
    def __init__(self) -> None:
        self.counter = 0

    def increment(self):
        self.counter += 1

    def decrement(self):
        self.counter -= 1


d = Data()


def main(page):
    page.snack_bar = ft.SnackBar(
        content=ft.Text(f"You did it!"),
        action="Undo it!",
        on_action=lambda e: d.decrement(),
    )

    def on_click(e):
        d.increment()
        page.snack_bar.content.value = f"You did it x {d.counter}"
        page.snack_bar.open = True
        page.update()

    page.add(ft.ElevatedButton("Open SnackBar", on_click=on_click))


ft.app(main)
