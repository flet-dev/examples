import flet as ft


class Data:
    def __init__(self) -> None:
        self.counter = 0

    def increment(self):
        self.counter += 1

    def decrement(self):
        self.counter -= 1


d = Data()


def main(page):
    page.title = "SnackBar examples"

    sb = ft.SnackBar(
        content=ft.Text(f"You did it!"),
        action="Undo it!",
        on_action=lambda e: d.decrement(),
    )

    def on_click(e):
        d.increment()
        sb.content.value = f"You did it x {d.counter}"
        page.open(sb)
        page.update()

    page.add(ft.ElevatedButton("Open SnackBar", on_click=on_click))


ft.app(main)
