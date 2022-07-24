from dataclasses import dataclass

import flet
from flet import AlertDialog, Column, ElevatedButton, Page, Row, Text, TextField, colors


@dataclass
class Message:
    user: str
    text: str


def main(page: Page):

    chat = Column()
    new_message = TextField()

    def on_message(message: Message):
        if message.user != None:
            chat.controls.append(Text(f"{message.user}: {message.text}"))
        else:
            chat.controls.append(
                Text(message.text, italic=True, color=colors.BLACK45, size=12)
            )
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(e):
        page.pubsub.send_all(Message(page.user, new_message.value))
        new_message.value = ""
        page.update()

    user_name = TextField(label="Enter your name")

    page.user = page.session_id

    def join_click(e):
        if not user_name.value:
            user_name.error_text = "Name cannot be blank!"
            user_name.update()
        else:
            page.user = user_name.value
            page.dialog.open = False
            page.pubsub.send_all(Message(None, f"{page.user} has joined the chat."))
            page.update()

    page.dialog = AlertDialog(
        open=True,
        modal=True,
        title=Text("Welcome!"),
        content=Column([user_name], tight=True),
        actions=[ElevatedButton(text="Join chat", on_click=join_click)],
        actions_alignment="end",
    )

    page.add(chat, Row([new_message, ElevatedButton("Send", on_click=send_click)]))


flet.app(target=main, view=flet.WEB_BROWSER)
