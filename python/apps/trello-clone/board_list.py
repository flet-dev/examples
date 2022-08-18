from flet import (
    UserControl,
    Draggable,
    Column,
    Row,
    Switch,
    Checkbox,
    Text,
    FloatingActionButton,
    Container,
    TextButton,
    TextField,
    IconButton,
    Card,
    icons,
    border_radius,
    colors,
    padding,
    margin
)


class BoardList(UserControl):
    def __init__(self, board, title: str, color: str = ""):
        super().__init__()
        self.board = board
        self.title = title
        self.color = color
        #self.card_list = []

    def build(self):

        def edit_title(e):
            self.header.controls[0] = edit_field
            self.header.controls[1].visible = False
            self.header.controls[2].visible = False
            self.update()

        def delete_list(e):
            self.board.remove_list(self, e)

        def save_title(e):
            self.title = edit_field.controls[0].value
            self.header.controls[0] = Text(
                value=self.title, style="titleMedium")
            self.header.controls[1].visible = True
            self.header.controls[2].visible = True
            self.update()

        def add_card(self, e):
            # self.hrztlCardList.controls.insert(
            #     -1,
            #     Checkbox(
            #         label=self.cardInput.value, on_change=self.card_checked_H)
            # )

            # self.vrtclCardList.controls.insert(
            #     -1,
            #     Checkbox(
            #         label=self.cardInput.value, on_change=self.card_checked_V)
            # )

            #self.cardInput.value = ""
            self.update()

        edit_field = Row([
            TextField(label=self.title),
            TextButton(text="Save", on_click=save_title)
        ])
        self.header = Row(

            alignment="spaceBetween",
            controls=[
                Text(value=self.title, style="titleMedium"),
                IconButton(
                    icon=icons.CREATE_OUTLINED,
                    tooltip="Edit List Title",
                    on_click=edit_title,
                ),
                IconButton(
                    icons.DELETE_OUTLINE,
                    tooltip="Delete List",
                    on_click=delete_list,
                ),
            ],
        )

        self.view = Draggable(
            group="lists",
            content=Column([
                self.header,
                Container(
                    content=Column([
                        TextField(label="new card name", width=200),
                        TextButton(
                            "add card", icon=icons.ADD, on_click=add_card)]),
                    # border_radius=border_radius.all(15),
                    bgcolor=self.color if (
                        self.color != "") else colors.BACKGROUND,
                    padding=padding.all(20)
                )

            ], data=self.title)
        )

        return self.view

    def card_checked(self, e):
        print("card_checked event: ", e.control)
        # i = self.board.boardListsHash[self.title][0].cardList.controls.index(
        #     e.control)
        # self.board.boardListsHash[self.title][1].cardList.controls[i].value = e.control.value
        pass
