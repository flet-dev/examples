import flet as ft


def main(page: ft.Page):
    def dropdown_changed(e):
        t.value = f"Dropdown changed to {dd.value}"
        page.update()

    t = ft.Text()
    dd = ft.DropdownM2(
        on_change=dropdown_changed,
        options=[
            ft.dropdownm2.Option("Red"),
            ft.dropdownm2.Option("Green"),
            ft.dropdownm2.Option("Blue"),
        ],
        width=200,
    )
    page.add(dd, t)


ft.run(main)
