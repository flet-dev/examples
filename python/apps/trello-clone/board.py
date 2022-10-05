import itertools
from flet import (
    DragTarget,
    Draggable,
    UserControl,
    Column,
    Row,
    FloatingActionButton,
    Text,
    Switch,
    GridView,
    Image,
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
    id_counter = itertools.count()

    def __init__(self, app, identifier: str):
        super().__init__()
        self.board_id = next(BoardList.id_counter)
        self.app = app
        self.visible = False
        self.identifier = identifier
        self.add_list_button = FloatingActionButton(
            icon=icons.ADD, text="add a list", height=30, on_click=self.addListDlg)

        self.board_lists = [
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
        for l in self.app.store.get_lists_by_board(self.board_id):
            self.add_list(l)

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
            padding=padding.only(top=10),
            height=self.app.page.height,
        )
        return self.view

    # def construct_board_layout(self):
    #     # retrieve all board_lists from data layer and ensure that they are interspersed with dividers etc.
    #     lists_from_store = self.app.store.get_lists_by_board(self.board_id)
    #     for i in range(len(lists_from_store)):
    #         print("list_from_store: ", i, lists_from_store[i])
    #         self.board_lists.insert(i+1, lists_from_store[i])
    #         self.board_lists.insert(i+1, Container(
    #             bgcolor=colors.BLACK26,
    #             border_radius=border_radius.all(30),
    #             height=100,
    #             alignment=alignment.center_right,
    #             width=3,
    #             opacity=0.0
    #         ))

    def resize(self, width, height):
        self.list_wrap.width = width
        self.view.height = height
        self.list_wrap.update()
        self.view.update()

    def addListDlg(self, e):

        option_dict = {
            colors.LIGHT_GREEN: self.color_option_creator(colors.LIGHT_GREEN, "green"),
            colors.RED_200: self.color_option_creator(colors.RED_200, "red"),
            colors.PINK_300: self.color_option_creator(colors.PINK_300, "pink"),
            colors.AMBER_500: self.color_option_creator(colors.AMBER_500, "amber"),
            colors.ORANGE_300: self.color_option_creator(colors.ORANGE_300, "orange"),
            colors.DEEP_ORANGE_300: self.color_option_creator(colors.DEEP_ORANGE_300, "orange"),
            colors.GREEN_400: self.color_option_creator(colors.GREEN_400, "green"),
            colors.TEAL_500: self.color_option_creator(colors.TEAL_500, "teal"),
            colors.YELLOW_400: self.color_option_creator(colors.YELLOW_400, "yellow"),
            colors.LIGHT_BLUE: self.color_option_creator(colors.LIGHT_BLUE, "blue"),
            colors.PURPLE_400: self.color_option_creator(colors.PURPLE_400, "purple"),
            colors.BROWN_300: self.color_option_creator(colors.BROWN_300, "brown"),
            colors.CYAN_500: self.color_option_creator(colors.CYAN_500, "cyan"),
            colors.BLUE_GREY_500: self.color_option_creator(colors.BLUE_GREY_500, "blue"),
            colors.GREEN_500: self.color_option_creator(colors.GREEN_500, "green"),
        }

        def set_color(e):
            print("e.control.data: ", e.control, e.control.data)
            chosen_color = e.control.data
            color_options.data = chosen_color
            #print("colorOptions.data: ", color_options.data)
            for k, v in option_dict.items():
                if k == e.control.data:
                    #v.bgcolor = colors.BLACK12
                    v.border = border.all(3, colors.BLACK26)
                    #v.border_radius = border_radius.all(100)
                else:
                    v.border = None
            dialog.content.update()

        #color_options = Row(data="")
        color_options = GridView(
            runs_count=3, max_extent=40, data="", height=150)

        # for k, v in option_dict.items():
        #     color_options.controls.append(
        #         TextButton(
        #             content=v,
        #             on_click=set_color,
        #             data=k
        #         )
        #     )
        for _, v in option_dict.items():
            v.on_click = set_color
            color_options.controls.append(v)

        def close_dlg(e):
            new_list = BoardList(self, e.control.value,
                                 color=color_options.data)
            self.add_list(new_list)
            self.app.store.add_list(self.board_id, new_list)
            # self.construct_board_layout()
            dialog.open = False
            self.app.page.update()
            self.update()

        dialog = AlertDialog(
            title=Text("Name your new list"),
            content=Column([
                Container(content=TextField(label="New List Name", on_submit=close_dlg),
                          padding=padding.symmetric(horizontal=5)),
                color_options
            ], tight=True, alignment="center"),

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
        self.app.store.remove_list(self.board_id, list.board_list_id)
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
            bgcolor=color,
            border_radius=border_radius.all(50),
            height=10,
            width=10,
            padding=padding.all(5),
            alignment=alignment.center,
            data=color
        )
