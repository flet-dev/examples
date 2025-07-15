import flet as ft


def main(page: ft.Page):
    def find_option(option_name):
        for option in d.options:
            if option_name == option.key:
                return option
        return None

    def handle_add(e: ft.Event[ft.ElevatedButton]):
        d.options.append(ft.dropdownm2.Option(option_textbox.value))
        d.value = option_textbox.value
        option_textbox.value = ""
        page.update()

    def handle_delete(e: ft.Event[ft.OutlinedButton]):
        option = find_option(d.value)
        if option is not None:
            d.options.remove(option)
            # d.value = None
            page.update()

    page.add(
        d := ft.DropdownM2(options=[], color=ft.Colors.BLUE_400),
        ft.Row(
            controls=[
                option_textbox := ft.TextField(hint_text="Enter item name"),
                ft.ElevatedButton(content="Add", on_click=handle_add),
                ft.OutlinedButton(
                    content="Delete selected",
                    on_click=handle_delete,
                    style=ft.ButtonStyle(bgcolor=ft.Colors.RED),
                ),
            ]
        ),
    )


ft.run(main)
