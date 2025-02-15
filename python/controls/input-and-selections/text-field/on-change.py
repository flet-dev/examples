import flet
from flet import ElevatedButton, Page, Text, TextField


def main(page: Page):
    def textbox_changed(e):
        t.value = e.control.value
        page.update()

    t = Text()
    tb = TextField(
        label="Textbox with 'change' event:",
        on_change=textbox_changed,
    )

    page.add(tb, t)


flet.app(target=main)
