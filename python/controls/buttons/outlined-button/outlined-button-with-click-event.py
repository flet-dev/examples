import flet
from flet import OutlinedButton, Page, Text


def main(page: Page):
    page.title = "Outlined button with 'click' event"

    def button_clicked(e):
        b.data += 1
        t.value = f"Button clicked {b.data} time(s)"
        page.update()

    b = OutlinedButton("Button with 'click' event", on_click=button_clicked, data=0)
    t = Text()

    page.add(b, t)


flet.app(target=main)
