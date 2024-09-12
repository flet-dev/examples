from time import sleep

import flet
from flet import ElevatedButton, ProgressBar


def main(page):
    def button_click(e):
        page.overlay.append(ProgressBar())
        btn.disabled = True
        page.update()
        sleep(3)
        page.overlay.clear()
        btn.disabled = False
        page.update()

    btn = ElevatedButton("Do some lengthy task!", on_click=button_click)

    page.add(btn)


flet.app(target=main)
