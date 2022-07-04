import flet
from flet import Column, ElevatedButton, Page, Row, Text, TextField


def main(page: Page):
    chat = Column()
    new_message = TextField()

    def send_click(e):
        chat.controls.append(Text(new_message.value))
        new_message.value = ""
        page.update()

    page.add(
        chat, Row(controls=[new_message, ElevatedButton("Send", on_click=send_click)])
    )


flet.app("chat", target=main)
