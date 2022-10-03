from mimetypes import init
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

    def update_board(self, board: Board, update: dict):
        print("board to update: ", board)
        initial_key = board.identifier
        for k in update:
            print("update_board: ", k, update[k])
            setattr(board, k, update[k])

        self.boards[board.identifier] = board
        del self.boards[initial_key]
        print("memory store boards: ", self.boards)

    def get_boards(self):
        return [self.boards[b] for b in self.boards]

    def remove_board(self, board: Board):
        print("board passed to memory store: ", board, board.identifier)
        print("memory store boards: ", self.boards)
        del self.boards[board.identifier]

    def add_list(self, board: str, list: BoardList):
        self.board_lists[board].append(list)

    def get_lists_by_board(self, board: str):
        return self.board_lists[board]

    def remove_list(self, board: str, id: int):
        self.board_lists[board] = [
            l for l in self.board_lists[board] if l.board_list_id == id]
