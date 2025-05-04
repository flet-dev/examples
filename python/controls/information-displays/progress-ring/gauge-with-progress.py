import flet as ft


def main(page: ft.Page):

    page.add(
        ft.Stack(
            [
                ft.Container(ft.Text("60%"), alignment=ft.Alignment.center()),
                ft.ProgressRing(
                    value=0.6,
                    width=100,
                    height=100,
                ),
            ],
            width=100,
            height=100,
        )
    )


ft.app(target=main)
