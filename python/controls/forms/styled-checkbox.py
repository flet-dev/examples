import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Checkbox(label="Checkbox with default style"),
        ft.Checkbox(
            label="Checkbox with constant fill color",
            fill_color="red",
            check_color="yellow",
        ),
        ft.Checkbox(
            label="Checkbox with dynamic fill color",
            fill_color={
                ft.MaterialState.HOVERED: "blue",
                ft.MaterialState.SELECTED: "green",
                ft.MaterialState.DEFAULT: "red",
            },
        ),
    )


ft.app(main)
