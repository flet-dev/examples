import flet as ft


def main(page: ft.Page):
    flashlight = ft.Flashlight()
    page.overlay.append(flashlight)
    page.add(ft.TextButton("toggle", on_click=lambda _: flashlight.toggle()))


ft.app(main)
