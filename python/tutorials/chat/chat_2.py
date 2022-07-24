from dataclasses import dataclass

import flet
from flet import Column, ElevatedButton, Page, Row, Text, TextField


@dataclass
class Message:
    user: str
    text: str


def main(page: Page):

    chat = Column()
    new_message = TextField()

    def on_message(message: Message):
        chat.controls.append(Text(f"{message.user}: {message.text}"))
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(e):
        page.pubsub.send_all(Message(page.session_id, new_message.value))
        new_message.value = ""
        page.update()

    page.add(chat, Row([new_message, ElevatedButton("Send", on_click=send_click)]))


flet.app(target=main, view=flet.WEB_BROWSER)
