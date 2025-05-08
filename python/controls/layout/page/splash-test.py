from time import sleep
import flet as ft


def main(page: ft.Page):
    def button_click(e):
        my_bar = ft.ProgressBar()

        page.overlay.append(my_bar)
        btn.disabled = True
        page.update()
        sleep(3)

        page.overlay.remove(my_bar)
        btn.disabled = False
        page.update()

    btn = ft.ElevatedButton("Do some lengthy task!", on_click=button_click)
    page.add(btn)


ft.run(main)
