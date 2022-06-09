import logging

import flet
from flet import (
    AlertDialog,
    Column,
    Container,
    ElevatedButton,
    IconButton,
    ListView,
    Page,
    Row,
    Text,
    TextField,
    border,
    border_radius,
    colors,
    icons,
    padding,
)

pub_sub = {}

# logging.basicConfig(level=logging.DEBUG)


def broadcast(user, message):
    for session_id, handler in pub_sub.items():
        handler(user, message)


def main(page: Page):
    page.bgcolor = colors.SURFACE_VARIANT
    page.horizontal_alignment = "stretch"
    page.title = "Flet Chat"
    page.user = page.session_id

    def client_exited(e):
        print("A user left the chat")

    page.on_close = client_exited

    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error_text = "Name cannot be blank!"
            join_user_name.update()
        else:
            page.user = join_user_name.value
            page.dialog.open = False
            page.update()

    def send_message_click(e):
        broadcast(page.user, message.value)
        print(page.user, message.value)
        message.value = ""
        message.focus()
        page.update()

    def on_message(user, message):
        print("sdfsfsdfsdsdf")
        messages.controls.append(Text(f"{user}: {message}"))
        page.update()

    pub_sub[page.session_id] = on_message

    # A dialog asking user for chat display name
    join_user_name = TextField(
        label="Enter your name to join the chat",
        autofocus=True,
        on_submit=join_chat_click,
    )
    page.dialog = AlertDialog(
        open=True,
        modal=True,
        title=Text("Welcome!"),
        content=Column([join_user_name], width=300, height=70, tight=True),
        actions=[ElevatedButton(text="Join chat", on_click=join_chat_click)],
        actions_alignment="end",
    )

    # Chat messages
    messages = ListView(
        expand=True,
        spacing=0,
        divider_thickness=0,
        auto_scroll=True,
    )

    # A new message entry form
    message = TextField(
        hint_text="Write a message...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_message_click,
    )
    send = IconButton(
        icon=icons.SEND_ROUNDED, tooltip="Send message", on_click=send_message_click
    )
    form = Row([message, send])

    # Add everything to the page
    page.add(
        Container(
            content=messages,
            bgcolor=colors.SURFACE,
            border=border.all(1, colors.OUTLINE),
            border_radius=border_radius.all(5),
            padding=padding.all(10),
            expand=True,
        ),
        form,
    )


flet.app(port=8550, target=main, view=flet.WEB_BROWSER)
