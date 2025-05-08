import flet as ft


def main(page: ft.Page):
    page.add(
        ft.DropdownM2(
            label="Color",
            hint_text="Choose your favourite color?",
            options=[
                ft.dropdownm2.Option("Red"),
                ft.dropdownm2.Option("Green"),
                ft.dropdownm2.Option("Blue"),
            ],
            autofocus=True,
        )
    )


ft.run(main)
