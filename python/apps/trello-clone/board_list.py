from flet import (
    UserControl,
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
    def __init__(self, board, title: str, horizontal: bool, color: str = ""):
        super().__init__()
        self.board = board
        self.horizontal = horizontal
        self.title = title
        self.color = color

    def build(self):

        def edit_title(self, e):
            self.header.controls[0] = editField
            self.header.controls[1].visible = False
            self.header.controls[2].visible = False
            self.update()

        def delete_list(self, e):
            self.board.removeList(self, e)

        def save_title(self, e):
            self.title = editField.controls[0].value
            self.header.controls[0] = Text(
                value=self.title, style="titleMedium")
            self.header.controls[1].visible = True
            self.header.controls[2].visible = True
            self.update()

        def addCard(self, e):
            self.hrztlCardList.controls.insert(
                -1,
                Checkbox(
                    label=self.cardInput.value, on_change=self.card_checked_H)
            )

            self.vrtclCardList.controls.insert(
                -1,
                Checkbox(
                    label=self.cardInput.value, on_change=self.card_checked_V)
            )

            self.cardInput.value = ""
            self.update()

        editField = Row([
            TextField(label=self.title),
            TextButton(text="Save", on_click=save_title)
        ])
        cardInput = TextField(label="new card name", width=200)
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

        hrztlCardList = Row([cardInput, TextButton(
            "add card", icon=icons.ADD, on_click=self.addCard)])

        vrtclCardList = Column([cardInput, TextButton(
            "add card", icon=icons.ADD, on_click=self.addCard)])

        # list = Column([
        #     Row([cardInput, TextButton(
        #         "add card", icon=icons.ADD, on_click=addCard)], visible=(self.horizontal)),
        #     Column([cardInput, TextButton(
        #         "add card", icon=icons.ADD, on_click=addCard)], visible=(not self.horizontal))
        # ])

        self.view = Column([
            self.header,
            Container(
                content=hrztlCardList,
                # border_radius=border_radius.all(15),
                bgcolor=self.color if (
                    self.color != "") else colors.BACKGROUND,
                padding=padding.all(20),
                visible=self.horizontal
            ),
            Container(
                content=vrtclCardList,
                # border_radius=border_radius.all(15),
                bgcolor=self.color if (
                    self.color != "") else colors.BACKGROUND,
                padding=padding.all(20),
                visible=(not self.horizontal)
            )

        ], data=self.title)

        return self.view

    def toggleView(self):
        self.horizontal = (not self.horizontal)
        self.view.controls[1].visible = (self.horizontal)
        self.view.controls[2].visible = (not self.horizontal)
        self.update()

    def addCard(self, e):
        self.hrztlCardList.controls.insert(
            -1,
            Checkbox(
                label=self.cardInput.value, on_change=self.card_checked_H)
        )

        self.vrtclCardList.controls.insert(
            -1,
            Checkbox(
                label=self.cardInput.value, on_change=self.card_checked_V)
        )

        self.cardInput.value = ""
        self.update()

    def card_checked_H(self, e):
        print("card_checked event: ", e.control)
        i = self.board.boardListsHash[self.title][0].cardList.controls.index(
            e.control)
        self.board.boardListsHash[self.title][1].cardList.controls[i].value = e.control.value
        pass

    def card_checked_V(self, e):
        print("card_checked event: ", e.control)
        i = self.board.boardListsHash[self.title][1].cardList.controls.index(
            e.control)
        self.board.boardListsHash[self.title][0].cardList.controls[i].value = e.control.value
        pass

    # def buildList(self):
    #     return Container(
    #         content=Column(controls=self.cardList, expand=True),
    #         border_radius=border_radius.all(15),
    #         bgcolor=colors.WHITE24,
    #         padding=padding.all(20),
    #         margin=margin.all(10),
    #     )
