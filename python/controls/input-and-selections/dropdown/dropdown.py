import logging
import flet as ft

logging.basicConfig(level=logging.INFO)


def main(page: ft.Page):
    dd = ft.Dropdown(
        options=[
            ft.dropdown.Option("a", "Item A"),
            ft.dropdown.Option("b", "Item B"),
            ft.dropdown.Option("c", "Item C"),
        ]
    )

    def btn2_click(e):
        dd.options.append(ft.dropdown.Option("d", "Item D"))
        page.update()

    def btn3_click(e):
        dd.options[1].text = "Item Blah Blah Blah"
        page.update()

    btn2 = ft.ElevatedButton("Add new item!", on_click=btn2_click)
    btn3 = ft.ElevatedButton("Change second item", on_click=btn3_click)

    page.add(dd, btn2, btn3)


ft.app(main)
