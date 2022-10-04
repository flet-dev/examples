from mimetypes import init
from board import Board
from user import User
from board_list import BoardList
from data_store import DataStore
from flet import (Page)


class InMemoryStore(DataStore):
    def __init__(self, page: Page):
        self.page = page
        self.boards: dict[int, Board] = {}
        self.users: dict[str, User] = {}
        self.board_lists: dict[int, list[BoardList]] = {}

    def add_board(self, board: Board):
        self.boards[board.board_id] = board
        # self.board_lists[0] = [BoardList(self.boards[0], "test", "Red"), BoardList(
        #     self.boards[0], "test2", "Blue")]

    def get_board(self, id: int):
        return self.boards[id]

    def update_board(self, board: Board, update: dict):
        #initial_key = board.identifier
        for k in update:
            setattr(board, k, update[k])
        #self.boards[board.identifier] = board
        #del self.boards[initial_key]

    def get_boards(self):
        return [self.boards[b] for b in self.boards]

    def remove_board(self, board: Board):
        del self.boards[board.board_id]
        self.board_lists[board.board_id] = []

    def add_list(self, board: int, list: BoardList):
        if board in self.board_lists:
            print("already found")
            self.board_lists[board].append(list)
        else:
            print("first time")
            self.board_lists[board] = [list]
        print("memory store board_lists: ", self.board_lists)

    def get_lists_by_board(self, board: int):
        return self.board_lists.get(board, [])

    def remove_list(self, board: int, id: int):
        self.board_lists[board] = [
            l for l in self.board_lists[board] if not l.board_list_id == id]
        print("self.board_lists[board]: ", self.board_lists[board])
