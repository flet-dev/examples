
from chat import Chat, Message, User

class Fletogram():
    def __init__(self, on_chat_clicked):
        super().__init__()
        self.chats = []
        self.users = []
        self.on_chat_clicked = on_chat_clicked
        self.generate_users()
        self.generate_group_chats()
        self.generate_individual_chats()

    
    def generate_users(self):
        self.users = [User(id=100, display_name='Inesa'),
                      User(id=101, display_name='Feodor'),
                      User(id=102, display_name='John')]
    
    def generate_group_chats(self):
    
        self.chats=[Chat(fletogram = self, name='work', title="Flet developers", messages=[
           Message(author=self.users[0], body="I have a question about adaptive design"),
           Message(author=self.users[1], body="?"),
           Message(author=self.users[0], body="What if it looks ugly?")
        ]),
        Chat(fletogram=self, name='Inesa', title="Inesa's stories", messages=[
           Message(author=self.users[0], body="Inesa Message 1 title is very long and boring"),
           Message(author=self.users[0], body="Inesa Message 1 title is very long and boring"),
           Message(author=self.users[0], body="Inesa Message 1 title is very long and boring and wouldn't fit into one line it will also not fit into two lines unfortunately")
        ]),
        Chat(fletogram=self, name='Saved', title="My saved messages")]
    
    def generate_individual_chats(self):
        for user in self.users:
            self.chats.append(Chat(fletogram=self, name=user.id, title = user.display_name))


    
    # def find_user(self, id):
    #     for user in self.users:
    #         if user.id==id:
    #             return user.display_name



    
