import flet as ft


def main(page: ft.Page):
    page.title = "Outlined button with 'click' event"
    page.theme_mode = ft.ThemeMode.LIGHT

    def button_clicked(e):
        b.data += 1
        t.value = f"Button clicked {b.data} time(s)"
        page.update()

    b = ft.OutlinedButton("Button with 'click' event", on_click=button_clicked, data=0)
    t = ft.Text()

    page.add(b, t)


ft.app(main)
