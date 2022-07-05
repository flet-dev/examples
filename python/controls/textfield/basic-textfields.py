import flet
from flet import ElevatedButton, Page, Text, TextField, icons


def main(page: Page):
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}', '{tb5.value}'."
        page.update()

    t = Text()
    tb1 = TextField(label="Standard")
    tb2 = TextField(label="Disabled", disabled=True, value="First name")
    tb3 = TextField(label="Read-only", read_only=True, value="Last name")
    tb4 = TextField(label="With placeholder", hint_text="Please enter text here")
    tb5 = TextField(label="With an icon", icon=icons.EMOJI_EMOTIONS)
    b = ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(tb1, tb2, tb3, tb4, tb5, b, t)


flet.app(target=main)
