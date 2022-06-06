import flet
from flet import Column, ElevatedButton, Page, Row, Text, TextField


def main(page: Page):
    messages = Column()
    message = TextField()

    def send_click(e):
        messages.controls.append(Text(message.value))
        message.value = ""
        page.update()

    send = ElevatedButton("Send", on_click=send_click)
    form = Row(controls=[message, send])
    page.add(messages, form)


flet.app("chat", target=main)
