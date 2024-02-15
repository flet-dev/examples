import flet as ft

from utils.generate_avatar import get_avatar_color, get_initials
from views.messages import Messages


class ChatTile(ft.ListTile):
    def __init__(self, chat):
        super().__init__()
        self.chat = chat
        self.leading = ft.CircleAvatar(
            content=ft.Text(get_initials(self.chat.display_name)),
            color=ft.colors.WHITE,
            bgcolor=get_avatar_color(self.chat.display_name),
        )
        self.title = ft.Text(chat.display_name)
        self.on_click = self.chat_tile_clicked
        self.generate_subtitle()

    def chat_tile_clicked(self, e):
        print("Chat clicked")
        messages_view = Messages(self.chat)
        e.control.page.views.append(messages_view)
        e.control.page.update()

    def generate_subtitle(self):
        """Show the body of the latest message"""
        if len(self.chat.messages) > 0:
            self.subtitle = ft.Text(
                max_lines=1,
                spans=[
                    ft.TextSpan(
                        text=f"{self.chat.messages[-1].author.display_name}: ",
                        style=ft.TextStyle(weight=ft.FontWeight.BOLD),
                    ),
                    ft.TextSpan(text=self.chat.messages[-1].body),
                ],
            )

        else:
            self.subtitle = ft.Text("No messages yet.")


class Chats(ft.View):
    def __init__(self, fletogram):
        super().__init__()
        self.route = "/"
        self.appbar = ft.AppBar(
            leading=ft.TextButton("Edit"),
            title=ft.Text("Chats"),
            actions=[
                ft.IconButton(icon=ft.icons.ADD_COMMENT),
            ],
        )
        self.fletogram = fletogram
        self.generate_chat_tiles()
        self.controls = [
            ft.ListView(
                spacing=0,
                controls=self.chat_tiles,
            )
        ]

        self.navigation_bar = self.fletogram.navigation_bar

    def generate_chat_tiles(self):
        self.chat_tiles = []
        for chat in self.fletogram.chats:
            self.chat_tiles.append(ChatTile(chat))
