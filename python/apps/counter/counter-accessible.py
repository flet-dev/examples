import flet
from flet import IconButton, Page, Row, Semantics, Text, TextField, icons
from flet.page import KeyboardEventData


def main(page: Page):
    page.title = "Flet counter example"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.spacing = 50

    def on_keyboard(e: KeyboardEventData):
        print(e)
        if e.key == "S" and e.ctrl:
            page.show_semantics_debugger = not page.show_semantics_debugger
            page.update()

    page.on_keyboard_event = on_keyboard

    txt_number = TextField(label="Number", value="0", text_align="right", width=100)
    sem = Semantics(txt_number, label="Current number: 0")

    def button_click(e):
        txt_number.value = int(txt_number.value) + (1 if e.control.data == "+" else -1)
        sem.label = f"Current number: {txt_number.value}"
        page.update()

    page.add(
        Row(
            [
                IconButton(
                    icons.REMOVE, tooltip="Decrement", on_click=button_click, data="-"
                ),
                sem,
                IconButton(
                    icons.ADD, tooltip="Increment", on_click=button_click, data="+"
                ),
            ],
            alignment="center",
        ),
        Text("Press CTRL+S to toggle semantics debugger"),
    )


flet.app(target=main)
