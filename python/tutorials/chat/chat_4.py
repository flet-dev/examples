import logging

import flet
from flet import (
    AlertDialog,
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    TextField,
    colors,
)

pub_sub = {}

logging.basicConfig(level=logging.DEBUG)


def broadcast(user, message):
    for session_id, handler in pub_sub.items():
        handler(user, message)


def main(page: Page):
    page.bgcolor = "#eeeeee"

    def send_click(e):
        broadcast(page.user, message.value)
        message.value = ""
        message.focus()
        page.update()

    messages = Column()
    message = TextField(
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        on_submit=send_click,
    )

    def on_message(user, message):
        messages.controls.append(Text(f"{user}: {message}"))
        page.update()

    pub_sub[page.session_id] = on_message

    def join_click(e):
        if not user_name.value:
            user_name.error_text = "Name cannot be blank!"
            user_name.update()
        else:
            page.user = user_name.value
            dlg.open = False
            page.update()

    user_name = TextField(label="Enter your name", autofocus=True, on_submit=join_click)

    page.user = page.session_id

    dlg = AlertDialog(
        open=True,
        modal=True,
        title=Text("Welcome!"),
        content=Column([user_name], width=300, height=70, tight=True),
        actions=[ElevatedButton(text="Join chat", on_click=join_click)],
        actions_alignment="end",
    )

    send = ElevatedButton("Send", on_click=send_click)
    form = Row([message, send])
    page.add(Container(content=messages, bgcolor=colors.SURFACE), form, dlg)


flet.app(port=8550, target=main, view=flet.WEB_BROWSER)
