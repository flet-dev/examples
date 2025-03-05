from time import sleep

import flet as ft


def main(page: ft.Page):

    page.add(ft.Text("Hello!"))
    sleep(3)
    page.window.visible = True
    page.update()


ft.app(main, view=ft.AppView.FLET_APP_HIDDEN)
