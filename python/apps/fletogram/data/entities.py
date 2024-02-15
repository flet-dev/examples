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


class Organization:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.members = []


class User:
    def __init__(self, id, display_name, first_name=None, last_name=None, avatar=None):
        self.id = id
        self.display_name = display_name
        self.first_name = first_name
        self.last_name = last_name
