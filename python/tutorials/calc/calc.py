import flet
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    border_radius,
    colors,
)


class CalcApp:
    def __init__(self):
        self.operator = "+"
        self.operand1 = 0
        self.operand2 = 0
        self.new_operand = True
        self.result = Text(value="0", color=colors.WHITE, size=20)

        # application's root control (i.e. "view") containing all other controls
        self.view = Container(
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(20),
            padding=20,
            content=Column(
                controls=[
                    Row(controls=[self.result], alignment="end"),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="AC",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="AC",
                            ),
                            ElevatedButton(
                                text="+/-",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="%",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="/",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                            ),
                        ],
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="7",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="7",
                            ),
                            ElevatedButton(
                                text="8",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="8",
                            ),
                            ElevatedButton(
                                text="9",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="9",
                            ),
                            ElevatedButton(
                                text="*",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="4",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="4",
                            ),
                            ElevatedButton(
                                text="5",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="5",
                            ),
                            ElevatedButton(
                                text="6",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="6",
                            ),
                            ElevatedButton(
                                text="-",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="1",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="1",
                            ),
                            ElevatedButton(
                                text="2",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="2",
                            ),
                            ElevatedButton(
                                text="3",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="3",
                            ),
                            ElevatedButton(
                                text="+",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="+",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="0",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=2,
                                on_click=self.button_clicked,
                                data="0",
                            ),
                            ElevatedButton(
                                text=".",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data=".",
                            ),
                            ElevatedButton(
                                text="=",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                ],
            ),
        )

    def button_clicked(self, e):
        if e.data == "AC":
            self.result.value = "0"

        elif e.data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == "0" or self.new_operand == True:
                self.result.value = e.data
                self.new_operand = False
            else:
                self.result.value = self.result.value + e.data

        elif e.data in ("+"):
            self.operator = e.data
            self.operand1 = float(self.result.value)
            self.new_operand = True

        self.view.update()


def main(page: Page):
    page.title = "Calc App"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.update()

    # create application instance
    app = CalcApp()

    # add application's root control to the page
    page.add(Column([app.view], width=300))


flet.app(target=main)
