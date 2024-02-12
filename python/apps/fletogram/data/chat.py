import flet as ft

from utils.generate_avatar import get_avatar_color, get_initials
from views.messages_view import MessagesView


class ChatMessage(ft.Container):
    def __init__(self, author, body, is_logged_user):
        super().__init__()
        self.author = author
        self.body = body
        self.is_logged_user = is_logged_user
        self.content = ft.Column()
        self.padding = 10
        self.expand = True
        self.expand_loose = True
        self.generate_message_display()

    def generate_message_display(self):
        if self.is_logged_user == False:
            self.bgcolor = ft.colors.GREY_100
            self.content.controls.append(
                ft.Text(self.author.display_name, weight=ft.FontWeight.BOLD)
            )
            self.border_radius = ft.border_radius.only(
                top_left=10, top_right=10, bottom_left=0, bottom_right=10
            )
        else:
            self.bgcolor = ft.colors.GREEN_100
            self.border_radius = ft.border_radius.only(
                top_left=10, top_right=10, bottom_left=10, bottom_right=0
            )
        self.content.controls.append(ft.Text(self.body))


class Chat(ft.ListTile):
    def __init__(self, name, display_name, fletogram, messages=[], group_chat=True):
        super().__init__()
        self.name = name
        self.display_name = display_name
        self.title = ft.Text(display_name)
        self.leading = ft.CircleAvatar(
            content=ft.Text(get_initials(self.display_name)),
            color=ft.colors.WHITE,
            bgcolor=get_avatar_color(self.display_name),
        )
        self.messages = messages
        self.fletogram = fletogram
        self.group_chat = group_chat
        self.members = []
        self.generate_subtitle()
        self.on_click = self.chat_clicked

    def add_message(self):
        """Adds message to the channel"""
        pass

    def chat_clicked(self, e):
        """Shows the latest message"""
        print("Chat clicked")
        messages_view = MessagesView(self)
        self.page.views.append(messages_view)
        self.page.update()

    def generate_subtitle(self):
        """Show the body of the latest message"""
        if len(self.messages) > 0:
            self.subtitle = ft.Text(
                max_lines=1,
                spans=[
                    ft.TextSpan(
                        text=f"{self.messages[-1].author.display_name}: ",
                        style=ft.TextStyle(weight=ft.FontWeight.BOLD),
                    ),
                    ft.TextSpan(text=self.messages[-1].body),
                ],
            )

        else:
            self.subtitle = ft.Text("No messages yet.")
