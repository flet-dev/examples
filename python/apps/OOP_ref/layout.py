import flet
from flet import Column, ElevatedButton, Text, TextField
from flet.ref import Ref

first_name = Ref[TextField]()
last_name = Ref[TextField]()
greetings = Ref[Column]()


def init_layout(page, logic={}):
    page.add(
        TextField(ref=first_name, label="First name", autofocus=True),
        TextField(ref=last_name, label="Last name"),
        ElevatedButton("Say hello!", on_click=logic.get('btn_click')),
        Column(ref=greetings),
    )


if __name__ == '__main__':
    flet.app(target=init_layout)
