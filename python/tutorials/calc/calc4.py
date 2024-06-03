import flet as ft

# from flet import (
#     Column,
#     Container,
#     ElevatedButton,
#     Page,
#     Row,
#     Text,
#     UserControl,
#     border_radius,
#     colors,
# )


class CalculatorApp(ft.Container):
    # def build(self):
    # application's root control (i.e. "view") containing all other controls
    def __init__(self):
        super().__init__()

        result = ft.Text(value="0", color=ft.colors.WHITE, size=20)
        self.width = 300
        self.bgcolor = ft.colors.BLACK
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20
        self.content = ft.Column(
            controls=[
                ft.Row(controls=[result], alignment="end"),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="AC",
                            bgcolor=ft.colors.BLUE_GREY_100,
                            color=ft.colors.BLACK,
                            expand=1,
                        ),
                        ft.ElevatedButton(
                            text="+/-",
                            bgcolor=ft.colors.BLUE_GREY_100,
                            color=ft.colors.BLACK,
                            expand=1,
                        ),
                        ft.ElevatedButton(
                            text="%",
                            bgcolor=ft.colors.BLUE_GREY_100,
                            color=ft.colors.BLACK,
                            expand=1,
                        ),
                        ft.ElevatedButton(
                            text="/",
                            bgcolor=ft.colors.ORANGE,
                            color=ft.colors.WHITE,
                            expand=1,
                        ),
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="7",
                            bgcolor=ft.colors.WHITE24,
                            color=ft.colors.WHITE,
                            expand=1,
                        ),
                        ft.ElevatedButton(
                            text="8",
                            bgcolor=ft.colors.WHITE24,
                            color=ft.colors.WHITE,
                            expand=1,
                        ),
                        ft.ElevatedButton(
                            text="9",
                            bgcolor=ft.colors.WHITE24,
                            color=ft.colors.WHITE,
                            expand=1,
                        ),
                        ft.ElevatedButton(
                            text="*",
                            bgcolor=ft.colors.ORANGE,
                            color=ft.colors.WHITE,
                            expand=1,
                        ),
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="4",
                            bgcolor=ft.colors.WHITE24,
                            color=ft.colors.WHITE,
                            expand=1,
                        ),
                        ft.ElevatedButton(
                            text="5",
                            bgcolor=ft.colors.WHITE24,
                            color=ft.colors.WHITE,
                            expand=1,
                        ),
                        ft.ElevatedButton(
                            text="6",
                            bgcolor=ft.colors.WHITE24,
                            color=ft.colors.WHITE,
                            expand=1,
                        ),
                        ft.ElevatedButton(
                            text="-",
                            bgcolor=ft.colors.ORANGE,
                            color=ft.colors.WHITE,
                            expand=1,
                        ),
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="1",
                            bgcolor=ft.colors.WHITE24,
                            color=ft.colors.WHITE,
                            expand=1,
                        ),
                        ft.ElevatedButton(
                            text="2",
                            bgcolor=ft.colors.WHITE24,
                            color=ft.colors.WHITE,
                            expand=1,
                        ),
                        ft.ElevatedButton(
                            text="3",
                            bgcolor=ft.colors.WHITE24,
                            color=ft.colors.WHITE,
                            expand=1,
                        ),
                        ft.ElevatedButton(
                            text="+",
                            bgcolor=ft.colors.ORANGE,
                            color=ft.colors.WHITE,
                            expand=1,
                        ),
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="0",
                            bgcolor=ft.colors.WHITE24,
                            color=ft.colors.WHITE,
                            expand=2,
                        ),
                        ft.ElevatedButton(
                            text=".",
                            bgcolor=ft.colors.WHITE24,
                            color=ft.colors.WHITE,
                            expand=1,
                        ),
                        ft.ElevatedButton(
                            text="=",
                            bgcolor=ft.colors.ORANGE,
                            color=ft.colors.WHITE,
                            expand=1,
                        ),
                    ]
                ),
            ]
        )

        # application's root control (i.e. "view") containing all other controls
        # return Container(
        #     width=300,
        #     bgcolor=colors.BLACK,
        #     border_radius=border_radius.all(20),
        #     padding=20,
        #     content=Column(
        #         controls=[
        #             Row(controls=[result], alignment="end"),
        #             Row(
        #                 controls=[
        #                     ElevatedButton(
        #                         text="AC",
        #                         bgcolor=colors.BLUE_GREY_100,
        #                         color=colors.BLACK,
        #                         expand=1,
        #                     ),
        #                     ElevatedButton(
        #                         text="+/-",
        #                         bgcolor=colors.BLUE_GREY_100,
        #                         color=colors.BLACK,
        #                         expand=1,
        #                     ),
        #                     ElevatedButton(
        #                         text="%",
        #                         bgcolor=colors.BLUE_GREY_100,
        #                         color=colors.BLACK,
        #                         expand=1,
        #                     ),
        #                     ElevatedButton(
        #                         text="/",
        #                         bgcolor=colors.ORANGE,
        #                         color=colors.WHITE,
        #                         expand=1,
        #                     ),
        #                 ]
        #             ),
        #             Row(
        #                 controls=[
        #                     ElevatedButton(
        #                         text="7",
        #                         bgcolor=colors.WHITE24,
        #                         color=colors.WHITE,
        #                         expand=1,
        #                     ),
        #                     ElevatedButton(
        #                         text="8",
        #                         bgcolor=colors.WHITE24,
        #                         color=colors.WHITE,
        #                         expand=1,
        #                     ),
        #                     ElevatedButton(
        #                         text="9",
        #                         bgcolor=colors.WHITE24,
        #                         color=colors.WHITE,
        #                         expand=1,
        #                     ),
        #                     ElevatedButton(
        #                         text="*",
        #                         bgcolor=colors.ORANGE,
        #                         color=colors.WHITE,
        #                         expand=1,
        #                     ),
        #                 ]
        #             ),
        #             Row(
        #                 controls=[
        #                     ElevatedButton(
        #                         text="4",
        #                         bgcolor=colors.WHITE24,
        #                         color=colors.WHITE,
        #                         expand=1,
        #                     ),
        #                     ElevatedButton(
        #                         text="5",
        #                         bgcolor=colors.WHITE24,
        #                         color=colors.WHITE,
        #                         expand=1,
        #                     ),
        #                     ElevatedButton(
        #                         text="6",
        #                         bgcolor=colors.WHITE24,
        #                         color=colors.WHITE,
        #                         expand=1,
        #                     ),
        #                     ElevatedButton(
        #                         text="-",
        #                         bgcolor=colors.ORANGE,
        #                         color=colors.WHITE,
        #                         expand=1,
        #                     ),
        #                 ]
        #             ),
        #             Row(
        #                 controls=[
        #                     ElevatedButton(
        #                         text="1",
        #                         bgcolor=colors.WHITE24,
        #                         color=colors.WHITE,
        #                         expand=1,
        #                     ),
        #                     ElevatedButton(
        #                         text="2",
        #                         bgcolor=colors.WHITE24,
        #                         color=colors.WHITE,
        #                         expand=1,
        #                     ),
        #                     ElevatedButton(
        #                         text="3",
        #                         bgcolor=colors.WHITE24,
        #                         color=colors.WHITE,
        #                         expand=1,
        #                     ),
        #                     ElevatedButton(
        #                         text="+",
        #                         bgcolor=colors.ORANGE,
        #                         color=colors.WHITE,
        #                         expand=1,
        #                     ),
        #                 ]
        #             ),
        #             Row(
        #                 controls=[
        #                     ElevatedButton(
        #                         text="0",
        #                         bgcolor=colors.WHITE24,
        #                         color=colors.WHITE,
        #                         expand=2,
        #                     ),
        #                     ElevatedButton(
        #                         text=".",
        #                         bgcolor=colors.WHITE24,
        #                         color=colors.WHITE,
        #                         expand=1,
        #                     ),
        #                     ElevatedButton(
        #                         text="=",
        #                         bgcolor=colors.ORANGE,
        #                         color=colors.WHITE,
        #                         expand=1,
        #                     ),
        #                 ]
        #             ),
        #         ]
        #     ),
        # )


def main(page: ft.Page):
    page.title = "Calc App"
    # create application instance
    calc = CalculatorApp()

    # add application's root control to the page
    page.add(calc)


ft.app(target=main)
