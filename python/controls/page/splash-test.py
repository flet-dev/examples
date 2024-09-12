from time import sleep
import flet as ft
from flet import ElevatedButton, ProgressBar

def main(page):
    def button_click(e):
        my_bar = ProgressBar()
        
        page.overlay.append(my_bar)
        btn.disabled = True
        page.update()
        sleep(3)

        page.overlay.remove(my_bar)
        btn.disabled = False
        page.update()

    btn = ElevatedButton("Do some lengthy task!", on_click=button_click)
    page.add(btn)

ft.app(target=main)
