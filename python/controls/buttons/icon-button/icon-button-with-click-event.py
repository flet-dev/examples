import flet as ft


def main(page: ft.Page):
    page.title = "Icon button with 'click' event"

    def button_clicked(e):
        b.data += 1
        t.value = f"Button clicked {b.data} time(s)"
        page.update()

    b = ft.IconButton(
        icon=ft.Icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=button_clicked, data=0
    )
    t = ft.Text()

    page.add(b, t)


ft.app(target=main)
