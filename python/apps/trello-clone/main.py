import logging
import os
from itertools import islice
from board import Board
import flet
from flet import (
    UserControl,
    AlertDialog,
    Column,
    Container,
    GridView,
    Icon,
    IconButton,
    Page,
    Row,
    SnackBar,
    Text,
    TextButton,
    IconButton,
    FloatingActionButton,
    NavigationRail,
    NavigationRailDestination,
    VerticalDivider,
    Divider,
    AppBar,
    Checkbox,
    ListTile,
    PopupMenuButton,
    PopupMenuItem,
    TextField,
    Switch,
    alignment,
    border_radius,
    colors,
    icons,
    padding,
    margin,
    border
)
#from dotenv import dotenv_values

#config = dotenv_values(".env.dev")

# trello app
# MVP  - Boards -> Lists -> Cards
# Views - Different views of boards (timeline, table, etc.)
# Boards contain a hash of board_lists (kept as horizontal/vertical tuples), therefore manage those lists (addition, deletion, editing, etc.)
# BoardLists contain Lists of cards, therefore manage those cards (addition, deletion, checked state etc.)


class TrelloApp:
    def __init__(self, page: Page):
        self.page = page
        self.sidebar = NavigationRail(
            destinations=[
                NavigationRailDestination(
                    padding=padding.all(5),
                    label_content=Text("Empty Board"),
                    selected_icon=icons.CHEVRON_RIGHT_ROUNDED
                )
            ],
            bgcolor=colors.LIGHT_GREEN_700,
            leading=Container(
                content=Row(
                    controls=[
                        TextButton("Add new board", icon=icons.ADD,
                                   on_click=self.addBoard),
                        # Text("Add new board", text_align="center", weight="w500"),
                        # IconButton(icon=icons.ADD, icon_size=20)
                    ]
                ),
                border_radius=border_radius.all(35),
                bgcolor=colors.WHITE12,
                padding=padding.all(0),
                margin=margin.all(0)
            ),
            on_change=self.navRail_change,
            selected_index=0,
            extended=True
        )

        self.boards = [
            Board(self, "Empty Board")
        ]
        self.currentBoardIndex: int = 0
        self.currentBoard = self.boards[self.currentBoardIndex]
        self.view = Row(
            [
                self.sidebar,
                VerticalDivider(width=2),
                self.currentBoard
            ],
            expand=True,
        )

    def update(self):
        self.currentBoard = self.boards[self.currentBoardIndex]
        self.page.update()
        # self.view.update()

    def navRail_change(self, e):
        self.currentBoardIndex = e.control.selected_index
        if self.currentBoard.mainView in self.view.controls:
            self.view.controls.remove(self.currentBoard.mainView)
        self.currentBoard = self.boards[e.control.selected_index]
        self.view.controls.append(self.currentBoard.mainView)
        #print("Selected destination: ", e.control.selected_index)
        self.view.update()

    def addBoard(self, e):
        def close_dlg(e):
            self.createNewBoard(e)
            dialog.open = False
            self.page.update()
        dialog = AlertDialog(
            title=Text("Name your new board"),
            content=Column(
                [TextField(label="New Board Name", on_submit=close_dlg)], tight=True),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def createNewBoard(self, e):

        self.sidebar.destinations.append(
            NavigationRailDestination(
                padding=padding.all(5),
                label_content=Text(e.control.value),
                label=e.control.value,
                selected_icon=icons.CHEVRON_RIGHT_ROUNDED
            )
        )
        newBoard = Board(self, e.control.value)
        self.boards.append(newBoard)
        self.view.controls.remove(self.boards[self.currentBoardIndex])
        self.currentBoardIndex = len(self.sidebar.destinations) - 1
        print("from createNewBoard - currentBoardIndex: ", self.currentBoardIndex)

        self.view.controls.append(self.boards[self.currentBoardIndex])
        self.sidebar.selected_index = self.currentBoardIndex
        self.update()


def main(page: Page):

    def search_app(e):
        "TODO"

    page.title = "Flet Trello clone"
    page.bgcolor = colors.LIGHT_GREEN_400
    page.appbar = AppBar(
        leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
        leading_width=100,
        title=Text("Trolli"),
        center_title=False,
        toolbar_height=75,
        bgcolor=colors.LIGHT_BLUE_ACCENT_700,
        actions=[
            Container(
                content=Row(
                    [
                        TextField(hint_text="Search this board", border="none",
                                  autofocus=False, on_submit=search_app, content_padding=padding.all(15), filled=False, suffix_icon=icons.SEARCH)
                    ],
                    alignment="spaceAround"
                ),
                bgcolor=colors.WHITE24,
                margin=margin.all(15),
                border=border.all(2, colors.WHITE),
                border_radius=border_radius.all(30)
            ),
            Container(
                content=PopupMenuButton(
                    items=[
                        PopupMenuItem(text="Profile"),
                        PopupMenuItem(),  # divider
                        PopupMenuItem(
                            text="Synchronize"
                        )
                    ]
                ),
                margin=margin.only(left=50, right=25)
            )
        ],
    )
    page.update()
    app = TrelloApp(page)
    page.add(app.view)
    # page.add(Text("Sanity Check"))


flet.app(target=main)
