from board import Board
from user import User
from board_list import BoardList
from data_store import DataStore
from flet import (Page)


class InMemoryStore(DataStore):
    def __init__(self, page: Page):
        self.page = page
        self.boards: dict[str, Board] = {}
        self.users: dict[str, User] = {}
        self.board_lists: dict[str, list[BoardList]] = {}

    def add_board(self, board: Board):
        self.boards[board.identifier] = board

    def get_board(self, id: str):
        return self.boards[id]

    def get_boards(self):
        return [self.boards[b] for b in self.boards]

    def remove_board(self, id: str):
        del self.boards[id]

    def add_list(self, board: str, list: BoardList):
        self.board_lists[board].append(list)

    def get_lists_by_board(self, board: str):
        return self.board_lists[board]

    def remove_list(self, board: str, id: int):
        self.board_lists[board] = [
            l for l in self.board_lists[board] if l.board_list_id == id]
