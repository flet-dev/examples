import flet
from flet import Column, ElevatedButton, Page, Row, Text, TextField

pub_sub = {}


def broadcast(user, message):
    for session_id, handler in pub_sub.items():
        handler(user, message)


def main(page: Page):

    messages = Column()
    message = TextField()

    def on_message(user, message):
        messages.controls.append(Text(f"{user}: {message}"))
        page.update()

    pub_sub[page.session_id] = on_message

    def send_click(e):
        broadcast(page.session_id, message.value)
        message.value = ""
        page.update()

    send = ElevatedButton("Send", on_click=send_click)
    form = Row([message, send])
    page.add(messages, form)


flet.app(target=main, view=flet.WEB_BROWSER)
