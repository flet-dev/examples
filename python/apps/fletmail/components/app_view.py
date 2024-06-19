import flet as ft
from model.messages import messages


class Message:
    def __init__(self, author, title, body, date, id):
        self.author = author
        self.title = title
        self.body = body
        self.date = date
        self.id = id


class AppView(ft.View):
    def __init__(self):
        super().__init__(route="/")
        self.__get_messages()
        self.selected_message_id = None

    def display_inbox(self): ...

    def display_chat(self): ...

    def display_meet(self): ...

    def display_message(self): ...

    def __get_messages(self):
        self.messages = []
        id = 1001
        for message in messages:
            self.messages.append(
                Message(
                    author=message["author"],
                    title=message["title"],
                    body=message["message"],
                    date=message["date"],
                    id=id,
                )
            )
            id += 1

    def get_message(self, id):
        for message in self.messages:
            if message.id == int(id):
                print("Found message!")
                return message

    # def display_inbox(self):
    #     print("Display inbox")
    #     self.mail_view.visible = True
    #     self.chat_view.visible = False
    #     self.meet_view.visible = False
    #     if self.selected_message_id == None:
    #         self.page.go("/inbox")
    #     else:
    #         self.page.go(f"/inbox/{self.selected_message_id}")

    # def display_chat(self):
    #     print("Display chat")
    #     self.mail_view.visible = False
    #     self.chat_view.visible = True
    #     self.meet_view.visible = False
    #     self.page.go("/chat")

    # def display_meet(self):
    #     print("Display meet")
    #     self.mail_view.visible = False
    #     self.chat_view.visible = False
    #     self.meet_view.visible = True
    #     self.page.go("/meet")
