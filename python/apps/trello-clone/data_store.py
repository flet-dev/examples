from board import Board
from board_list import BoardList
from user import User


class DataStore:

    def add_board(self, model) -> None:
        raise NotImplementedError

    def get_board(self, id) -> Board:
        raise NotImplementedError

    def get_boards(self) -> list[Board]:
        raise NotImplementedError

    def remove_board(self, id) -> None:
        raise NotImplementedError

    def add_user(self, model) -> None:
        raise NotImplementedError

    def get_users(self) -> list[User]:
        raise NotImplementedError

    def get_user(self, id) -> User:
        raise NotImplementedError

    def remove_user(self, id) -> None:
        raise NotImplementedError

    def add_list(self, board, model) -> None:
        raise NotImplementedError

    def get_lists(self) -> list[BoardList]:
        raise NotImplementedError

    def get_list(self, id) -> BoardList:
        raise NotImplementedError

    def get_lists_by_board(self, board) -> list[BoardList]:
        raise NotImplementedError

    def remove_list(self, id) -> None:
        raise NotImplementedError
