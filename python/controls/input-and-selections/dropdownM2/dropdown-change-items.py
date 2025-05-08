import flet as ft


def main(page: ft.Page):
    def find_option(option_name):
        for option in d.options:
            if option_name == option.key:
                return option
        return None

    def add_clicked(e):
        d.options.append(ft.dropdown.Option(option_textbox.value))
        d.value = option_textbox.value
        option_textbox.value = ""
        page.update()

    def delete_clicked(e):
        option = find_option(d.value)
        if option != None:
            d.options.remove(option)
            # d.value = None
            page.update()

    d = ft.DropdownM2()
    option_textbox = ft.TextField(hint_text="Enter item name")
    add = ft.ElevatedButton(content="Add", on_click=add_clicked)
    delete = ft.OutlinedButton(
        content="Delete selected",
        on_click=delete_clicked,
        style=ft.ButtonStyle(bgcolor=ft.Colors.RED),
    )
    page.add(d, ft.Row(controls=[option_textbox, add, delete]))


ft.run(main)
