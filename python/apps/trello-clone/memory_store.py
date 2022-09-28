from board import Board
from user import User
from board_list import BoardList
from data_store import DataStore
from flet import (Page)


class InMemoryStore(DataStore):

    # class BoardRepository(AbstractRepository):
    #     def __init__(self, page: Page):
    #         self.boards: list[Board] = []

    #     def add(self, board: Board):
    #         self.boards.append(board)

    #     def get_all(self):
    #         return self.boards

    #     def remove(self, board: Board):
    #         self.boards.pop(board)

    # class UserRepository(AbstractRepository):
    #     def __init__(self, page: Page):
    #         self.page: Page = page
    #         self.users: list[User] = []

    #     def list(self, user: User):
    #         return self.users

    #     def add(self, user: User):
    #         self.users.append(user)
