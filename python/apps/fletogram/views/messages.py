import flet as ft


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


class Messages(ft.View):
    def __init__(self, chat):
        super().__init__()
        self.route = "/chat"
        self.chat = chat
        self.appbar = ft.AppBar(
            title=ft.Text(self.chat.display_name),
            bgcolor=ft.colors.SURFACE_VARIANT,
        )
        self.generate_messages_view()

    def generate_messages_view(self):
        messages_view = ft.ListView(spacing=5)
        for message in self.chat.messages:
            if message.is_logged_user:
                alignment = ft.MainAxisAlignment.END
            else:
                alignment = ft.MainAxisAlignment.START
            messages_view.controls.append(
                ft.Row(
                    [message],
                    alignment=alignment,
                )
            )
            print(message.body)
        self.controls = [messages_view]
