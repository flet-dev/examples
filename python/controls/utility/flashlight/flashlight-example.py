import flet as ft
import flet_flashlight as ftf


def main(page: ft.Page):
    flashlight = ftf.Flashlight()
    page.overlay.append(flashlight)
    page.add(ft.TextButton("toggle", on_click=lambda _: flashlight.toggle()))


ft.run(main)
