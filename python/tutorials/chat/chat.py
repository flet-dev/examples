import logging
from dataclasses import dataclass

import flet
from flet import (
    AlertDialog,
    CircleAvatar,
    Column,
    Container,
    ElevatedButton,
    IconButton,
    ListView,
    Page,
    Row,
    Text,
    TextField,
    UserControl,
    border,
    colors,
    icons,
)

logging.basicConfig(level=logging.DEBUG)


@dataclass
class Message:
    user: str
    text: str


class ChatMessage(UserControl):
    def __init__(self, username: str, text: str):
        super().__init__()
        self.username = username
        self.text = text

    def get_initials(self):
        return self.username[:1].capitalize()

    def get_avatar_color(self, username: str):
        colors_lookup = [
            colors.AMBER,
            colors.BLUE,
            colors.BROWN,
            colors.CYAN,
            colors.GREEN,
            colors.INDIGO,
            colors.LIME,
            colors.ORANGE,
            colors.PINK,
            colors.PURPLE,
            colors.RED,
            colors.TEAL,
            colors.YELLOW,
        ]
        return colors_lookup[hash(username) % len(colors_lookup)]

    def build(self):
        return Row(
            [
                CircleAvatar(
                    content=Text(self.get_initials()),
                    color=colors.WHITE,
                    bgcolor=self.get_avatar_color(self.username),
                ),
                Column(
                    [
                        Text(self.username, weight="bold"),
                        Text(self.text, selectable=True),
                    ],
                    tight=True,
                    spacing=5,
                ),
            ],
            vertical_alignment="start",
        )


def main(page: Page):
    page.horizontal_alignment = "stretch"
    page.title = "Flet Chat"
    page.user = page.session_id

    def user_exited(e):
        print("A user left the chat")
        page.pubsub.unsubscribe_all()

    page.on_close = user_exited

    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error_text = "Name cannot be blank!"
            join_user_name.update()
        else:
            page.user = join_user_name.value
            page.dialog.open = False
            new_message.prefix = Text(f"{page.user}: ")
            page.pubsub.send_all(Message(None, f"{page.user} has joined the chat."))
            page.update()

    def send_message_click(e):
        if new_message.value != "":
            page.pubsub.send_all(Message(page.user, new_message.value))
            new_message.value = ""
            new_message.focus()
            page.update()

    def on_message(message: Message):
        if message.user != None:
            m = ChatMessage(message.user, message.text)
        else:
            m = Text(message.text, italic=True, color=colors.BLACK45, size=12)
        chat.controls.append(m)
        page.update()

    page.pubsub.subscribe(on_message)

    # A dialog asking for a user display name
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
    chat = ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    # A new message entry form
    new_message = TextField(
        hint_text="Write a message...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_message_click,
    )

    # Add everything to the page
    page.add(
        Container(
            content=chat,
            border=border.all(1, colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
        ),
        Row(
            [
                new_message,
                IconButton(
                    icon=icons.SEND_ROUNDED,
                    tooltip="Send message",
                    on_click=send_message_click,
                ),
            ]
        ),
    )


flet.app(port=8550, target=main, view=flet.WEB_BROWSER)
