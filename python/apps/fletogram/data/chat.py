import flet as ft


class ChatMessage(ft.Container):
    def __init__(self, author, body, is_logged_user):
        super().__init__()
        self.author = author
        self.body = body
        # self.width=250
        self.is_logged_user = is_logged_user
        self.content = ft.Column()
        self.border = ft.border.all(1, ft.colors.BLACK)
        self.bgcolor = ft.colors.GREEN_200
        self.padding = 10
        self.expand = True
        self.expand_loose = True
        self.generate_message_display()

    def generate_message_display(self):
        if self.is_logged_user == False:
            self.content.controls.append(
                ft.Text(self.author.display_name, weight=ft.FontWeight.BOLD)
            )
            self.border_radius = ft.border_radius.only(
                top_left=10, top_right=10, bottom_left=0, bottom_right=10
            )
        else:
            self.border_radius = ft.border_radius.only(
                top_left=10, top_right=10, bottom_left=10, bottom_right=0
            )
        self.content.controls.append(ft.Text(self.body))
        # self.content = ft.Text(self.body)


class Chat(ft.ListTile):
    def __init__(self, name, display_name, fletogram, messages=[], group_chat=True):
        super().__init__()
        # self.adaptive=True
        self.name = name
        self.display_name = display_name
        self.title = ft.Text(display_name)
        self.leading = ft.CircleAvatar(
            content=ft.Text(self.get_initials(self.display_name)),
            color=ft.colors.WHITE,
            bgcolor=self.get_avatar_color(self.display_name),
        )
        self.messages = messages
        self.fletogram = fletogram
        self.group_chat = group_chat
        self.members = []
        self.generate_subtitle()
        self.on_click = self.chat_clicked

    def get_initials(self, user_name: str):
        if user_name:
            return user_name[:1].capitalize()
        else:
            return "Unknown"  # or any default value you prefer

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]

    def add_message(self):
        """Adds message to the channel"""
        pass

    def chat_clicked(self, e):
        """Shows the latest message"""
        print("Chat clicked")
        messages_view = ft.ListView(spacing=5)
        for message in self.messages:
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

        self.page.views.append(
            ft.View(
                "/chat",
                [
                    ft.AppBar(
                        title=ft.Text(self.display_name),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    messages_view,
                ],
            )
        )
        self.page.update()
        # self.fletogram.on_chat_clicked(self)

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
