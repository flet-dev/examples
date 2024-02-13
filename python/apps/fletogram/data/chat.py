import flet as ft

# from utils.generate_avatar import get_avatar_color, get_initials

# from views.messages_view import MessagesView


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


class Chat:
    def __init__(self, name, display_name, fletogram, messages=[], group_chat=True):
        self.name = name
        self.display_name = display_name
        self.messages = messages
        self.fletogram = fletogram
        self.group_chat = group_chat
        self.members = []

    def add_message(self):
        """Adds message to the channel"""
        pass
