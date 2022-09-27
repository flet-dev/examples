from board import Board
from user import User
from board_list import BoardList
from flet import (Page)


class BoardRepository:
    def __init__(self, page: Page):
        self.boards: list[Board] = []

    def add(self, board: Board):
        self.boards.append(board)

    def get_all(self):
        return self.boards

    def remove(self, board: Board):
        self.boards.pop(board)


class UserRepository:
    def __init__(self, page: Page):
        self.page: Page = page
        self.users: list[User] = []

    def login(self, user: User):
        if user not in self.users:
            new_user = self.create(user.name, user.password)
            self.page.client_storage.set("current_user", new_user.name)
        else:
            self.page.client_storage.set("current_user", user.name)

    def create(self, user_name, password):
        new_user = User(user_name, password)
        self.users.append(new_user)
        return new_user
