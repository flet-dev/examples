import flet as ft

class Message():
    def __init__(self, author, body):
        self.author = author
        self.body=body

class Organization():
    def __init__(self, id, name):
        self.id=id
        self.name=name
        self.members=[]

class User(ft.ListTile):
    def __init__(self, id, display_name, first_name = None, last_name=None, avatar=None):
        super().__init__()
        self.adaptive = True,
        self.id = id
        self.display_name = display_name
        self.first_name = first_name
        self.last_name = last_name
        self.title = ft.Text(display_name)
        self.leading = ft.CircleAvatar(bgcolor=ft.colors.GREEN)


class Chat(ft.ListTile):
    def __init__(self, name, title, fletogram, messages=[], group_chat=True):
        super().__init__()
        self.adaptive=True
        self.name=name
        self.title = ft.Text(title)
        #self.leading = icon
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
        self.fletogram.on_chat_clicked(self)

    def generate_subtitle(self):
        """Show the body of the latest message"""
        if len(self.messages) >0:
            self.subtitle = ft.Text(max_lines=1, spans = [ft.TextSpan(text=f"{self.messages[-1].author.display_name}: ", style=ft.TextStyle(weight=ft.FontWeight.BOLD),), ft.TextSpan(text=self.messages[-1].body),
                                             ])