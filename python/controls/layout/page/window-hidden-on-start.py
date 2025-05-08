from time import sleep

import flet as ft


def main(page: ft.Page):

    page.add(ft.Text("Hello!"))
    sleep(3)
    page.window.visible = True
    page.update()


ft.run(main, view=ft.runView.FLET_APP_HIDDEN)
