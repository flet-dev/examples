import random
import flet as ft


def main(page: ft.Page):
    dd_options: list[ft.dropdownm2.Option] = []

    def dd_choice(e):
        t.value = f"{dd.value} chosen"
        page.update()

    def btn1_click(e):
        icon = ft.Icon(ft.Icons.random())
        dd_options.append(
            ft.dropdownm2.Option(text=f"{str(icon.name)[6:]}", content=icon)
        )
        page.update()

    def btn2_click(e):
        random.shuffle(dd_options)
        page.update()

    btn1 = ft.ElevatedButton("Add random item to dropdown!", on_click=btn1_click)
    btn2 = ft.ElevatedButton("Shuffle Dropdown items", on_click=btn2_click)
    dd = ft.DropdownM2(
        options=dd_options, options_fill_horizontally=True, on_change=dd_choice
    )
    t = ft.Text()

    page.add(dd, btn1, btn2, t)


ft.app(main)
