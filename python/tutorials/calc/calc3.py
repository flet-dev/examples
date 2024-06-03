import flet as ft

# from flet import (
#     Column,
#     Container,
#     ElevatedButton,
#     Page,
#     Row,
#     Text,
#     border_radius,
#     colors,
# )


def main(page: ft.Page):
    page.title = "Calc App"
    result = ft.Text(value="0", color=ft.colors.WHITE, size=20)

    page.add(
        ft.Container(
            width=300,
            bgcolor=ft.colors.BLACK,
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=ft.Column(
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
            ),
        )
    )


ft.app(target=main)
