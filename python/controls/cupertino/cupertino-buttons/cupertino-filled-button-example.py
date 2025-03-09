import flet as ft


def main(page: ft.Page):
    page.add(
        ft.CupertinoFilledButton(
            content=ft.Text("CupertinoFilled"),
            opacity_on_click=0.3,
            on_click=lambda e: print("CupertinoFilledButton clicked!"),
        ),
    )


ft.app(main)
