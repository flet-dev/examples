import flet as ft


def main(page: ft.Page):

    page.add(
        ft.Column(
            [
                ft.Container(
                    bgcolor=ft.Colors.AMBER,
                    alignment=ft.Alignment.center(),
                    expand=True,
                ),
                ft.Divider(),
                ft.Container(
                    bgcolor=ft.Colors.PINK, alignment=ft.Alignment.center(), expand=True
                ),
                ft.Divider(height=1, color="white"),
                ft.Container(
                    bgcolor=ft.Colors.BLUE_300,
                    alignment=ft.Alignment.center(),
                    expand=True,
                ),
                ft.Divider(height=9, thickness=3),
                ft.Container(
                    bgcolor=ft.Colors.DEEP_PURPLE_200,
                    alignment=ft.Alignment.center(),
                    expand=True,
                ),
            ],
            spacing=0,
            expand=True,
        ),
    )


ft.run(main)
