import logging
import random
import flet as ft

logging.basicConfig(level=logging.INFO)


def main(page: ft.Page):
    dd_options = []

    def dd_choice(e):
        t.value = f"{dd.value} chosen"
        page.update()

    def btn1_click(e):
        icon = ft.Icon(ft.Icons.random())
        dd.options.append(
            ft.dropdown.Option(text=f"{str(icon.name)[6:]}", content=icon)
        )
        page.update()

    def btn2_click(e):
        random.shuffle(dd_options)
        page.update()

    btn1 = ft.ElevatedButton("Add random item to dropdown!", on_click=btn1_click)
    btn2 = ft.ElevatedButton("Shuffle Dropdown items", on_click=btn2_click)
    dd = ft.Dropdown(options=dd_options, on_change=dd_choice)
    t = ft.Text()

    page.add(dd, btn1, btn2, t)


ft.app(main)
