import itertools
from flet import (
    UserControl,
    Column,
    Row,
    FloatingActionButton,
    ElevatedButton,
    Text,
    GridView,
    Container,
    TextField,
    AlertDialog,
    Container,
    icons,
    border_radius,
    border,
    colors,
    padding,
    alignment,
    margin
)
from board_list import BoardList
from data_store import DataStore


class Board(UserControl):
    id_counter = itertools.count()

    def __init__(self, app, store: DataStore, name: str):
        super().__init__()
        self.board_id = next(Board.id_counter)
        self.store: DataStore = store
        self.app = app
        self.name = name
        self.add_list_button = FloatingActionButton(
            icon=icons.ADD, text="add a list", height=30, on_click=self.create_list)

        self.board_lists = [
            self.add_list_button
        ]
        for l in self.store.get_lists_by_board(self.board_id):
            self.add_list(l)

        self.list_wrap = Row(
            self.board_lists,
            vertical_alignment="start",
            visible=True,
            scroll="auto",
            width=(self.app.page.width - 310),
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
            padding=padding.only(top=10, right=0),
            height=self.app.page.height,
        )
        return self.view

    def resize(self, nav_rail_extended, width, height):
        self.list_wrap.width = (
            width - 310) if nav_rail_extended else (width - 50)
        self.view.height = height
        self.list_wrap.update()
        self.view.update()

    def create_list(self, e):

        option_dict = {
            colors.LIGHT_GREEN: self.color_option_creator(colors.LIGHT_GREEN),
            colors.RED_200: self.color_option_creator(colors.RED_200),
            colors.AMBER_500: self.color_option_creator(colors.AMBER_500),
            colors.PINK_300: self.color_option_creator(colors.PINK_300),
            colors.ORANGE_300: self.color_option_creator(colors.ORANGE_300),
            colors.LIGHT_BLUE: self.color_option_creator(colors.LIGHT_BLUE),
            colors.DEEP_ORANGE_300: self.color_option_creator(colors.DEEP_ORANGE_300),
            colors.PURPLE_100: self.color_option_creator(colors.PURPLE_100),
            colors.RED_700: self.color_option_creator(colors.RED_700),
            colors.TEAL_500: self.color_option_creator(colors.TEAL_500),
            colors.YELLOW_400: self.color_option_creator(colors.YELLOW_400),
            colors.PURPLE_400: self.color_option_creator(colors.PURPLE_400),
            colors.BROWN_300: self.color_option_creator(colors.BROWN_300),
            colors.CYAN_500: self.color_option_creator(colors.CYAN_500),
            colors.BLUE_GREY_500: self.color_option_creator(colors.BLUE_GREY_500),
        }

        def set_color(e):
            color_options.data = e.control.data
            for k, v in option_dict.items():
                if k == e.control.data:
                    v.border = border.all(3, colors.BLACK26)
                else:
                    v.border = None
            dialog.content.update()

        color_options = GridView(
            runs_count=3, max_extent=40, data="", height=150)

        for _, v in option_dict.items():
            v.on_click = set_color
            color_options.controls.append(v)

        def close_dlg(e):
            if (hasattr(e.control, "text") and not e.control.text == "Cancel") or (type(e.control) is TextField and e.control.value != ""):
                new_list = BoardList(self, self.store, dialog_text.value,
                                     color=color_options.data)
                self.add_list(new_list)
            dialog.open = False
            self.page.update()
            self.update()

        def textfield_change(e):
            if dialog_text.value == "":
                create_button.disabled = True
            else:
                create_button.disabled = False
            self.page.update()
        dialog_text = TextField(label="New List Name",
                                on_submit=close_dlg, on_change=textfield_change)
        create_button = ElevatedButton(
            text="Create", bgcolor=colors.BLUE_200, on_click=close_dlg, disabled=True)
        dialog = AlertDialog(
            title=Text("Name your new list"),
            content=Column([
                Container(content=dialog_text,
                          padding=padding.symmetric(horizontal=5)),
                color_options,
                Row([
                    ElevatedButton(
                        text="Cancel", on_click=close_dlg),
                    create_button
                ], alignment="spaceBetween")
            ], tight=True, alignment="center"),

            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
        dialog_text.focus()

    def remove_list(self, list: BoardList, e):
        self.board_lists.remove(list)
        self.store.remove_list(self.board_id, list.board_list_id)
        self.update()

    def add_list(self, list: BoardList):
        self.board_lists.insert(-1, list)
        self.store.add_list(self.board_id, list)

    def color_option_creator(self, color: str):
        return Container(
            bgcolor=color,
            border_radius=border_radius.all(50),
            height=10,
            width=10,
            padding=padding.all(5),
            alignment=alignment.center,
            data=color
        )
