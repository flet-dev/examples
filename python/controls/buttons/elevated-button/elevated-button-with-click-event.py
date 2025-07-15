import flet as ft


def main(page: ft.Page):
    page.title = "Elevated button with 'click' event"
    page.theme_mode = ft.ThemeMode.LIGHT

    def button_clicked(e):
        button.data += 1
        message.value = f"Button clicked {button.data} time(s)"
        page.update()

    button = ft.ElevatedButton(
        content="Button with 'click' event",
        data=0,
        on_click=button_clicked,
    )
    message = ft.Text()

    page.add(button, message)


ft.run(main)
