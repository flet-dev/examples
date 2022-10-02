from flet import (
    DragTarget,
    Draggable,
    UserControl,
    Column,
    Row,
    FloatingActionButton,
    Text,
    Switch,
    Container,
    TextField,
    TextButton,
    AlertDialog,
    Container,
    Switch,
    Icon,
    icons,
    border_radius,
    border,
    colors,
    padding,
    alignment,
    margin
)
from board_list import BoardList


class Board(UserControl):

    def __init__(self, app, identifier: str):
        super().__init__()
        self.app = app
        self.visible = False
        self.identifier = identifier
        self.add_list_button = FloatingActionButton(
            icon=icons.ADD, text="add a list", height=30, on_click=self.addListDlg)
        self.board_lists = [
            # if this is an empty array then adding to it and updating component does not render a new list
            # why is a dummy control needed here? possible bug.
            # Text(visible=False)
            Container(
                bgcolor=colors.BLACK26,
                border_radius=border_radius.all(30),
                height=100,
                alignment=alignment.center_right,
                width=3,
                opacity=0.0
            ),
            self.add_list_button
        ]

        self.list_wrap = Row(
            self.board_lists,
            vertical_alignment="start",
            # wrap=True,
            visible=True,
            scroll="auto",
            # expand=True,
            width=(self.app.page.width - 330),
            height=(self.app.page.height - 95)
        )

    def build(self):
        self.view = Container(
            content=Column(
                controls=[
                    self.list_wrap
                ],

                scroll="auto",
                expand=True
            ),
            data=self,
            margin=margin.all(0),
            height=self.app.page.height,
        )
        return self.view

    def construct_board_layout():
        # retrieve all board_lists from data layer and ensure that they are interspersed with dividers etc.
        pass

    def resize(self, width, height):
        self.list_wrap.width = width
        self.view.height = height
        self.list_wrap.update()
        self.view.update()

    def addListDlg(self, e):

        option_dict = {
            colors.RED_200: self.color_option_creator(colors.RED_200, "red"),
            colors.LIGHT_GREEN: self.color_option_creator(colors.LIGHT_GREEN, "green"),
            colors.LIGHT_BLUE: self.color_option_creator(colors.LIGHT_BLUE, "blue"),
            colors.ORANGE_300: self.color_option_creator(colors.ORANGE_300, "orange"),
            colors.PINK_300: self.color_option_creator(colors.PINK_300, "pink"),
            colors.YELLOW_400: self.color_option_creator(colors.YELLOW_400, "yellow"),
        }

        def set_color(e):
            chosen_color = e.control.data
            color_options.data = chosen_color
            print("colorOptions.data: ", color_options.data)
            for k, v in option_dict.items():
                if k == e.control.data:
                    v.bgcolor = colors.BLACK12
                    # v.border = border.all(3, colors.BLACK26)
                    v.border_radius = border_radius.all(100)
                else:
                    v.bgcolor = None
            dialog.content.update()

        color_options = Row(data="")

        for k, v in option_dict.items():
            color_options.controls.append(
                TextButton(
                    content=v,
                    on_click=set_color,
                    data=k
                )
            )

        def close_dlg(e):
            new_list = BoardList(self, e.control.value,
                                 color=color_options.data)
            self.add_list(new_list)
            dialog.open = False
            self.app.page.update()
            self.update()

        dialog = AlertDialog(
            title=Text("Name your new list"),
            content=Column([
                Container(content=TextField(label="New List Name", on_submit=close_dlg),
                          padding=padding.symmetric(horizontal=5)),
                color_options
            ], tight=True),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.app.page.dialog = dialog
        dialog.open = True
        self.app.page.update()

    def remove_list(self, list: BoardList, e):
        # add confirmation ?
        i = self.board_lists.index(list)
        # delete both list and divider
        del self.board_lists[i:i+2]
        self.update()

    def add_list(self, list: BoardList):
        divider = Container(
            bgcolor=colors.BLACK26,
            border_radius=border_radius.all(30),
            height=100,
            alignment=alignment.center_right,
            width=3,
            opacity=0.0
        )
        #self.board_lists.insert(-1, new_list)
        # insert both list and divider
        self.board_lists[-1:-1] = [list, divider]

    def move_board(self, list: BoardList, displacement: int):
        i = self.boardList.index(list)
        listToMove = self.boardList.pop(i)
        self.boardList.insert(i + displacement, list)

    def color_option_creator(self, color: str, name: str):
        return Container(
            content=Column(
                [
                    Icon(name=icons.CIRCLE, color=color),
                    Text(
                        value=name,
                        # size=12,
                        width=50,
                        no_wrap=True,
                        text_align="center",

                    ),
                ],
                # spacing=5,
                alignment="center",
                horizontal_alignment="center",
            ),
            padding=padding.all(10),
            margin=margin.all(1),
            alignment=alignment.center,
        )
