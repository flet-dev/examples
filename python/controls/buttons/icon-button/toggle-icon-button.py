import flet as ft


def main(page: ft.Page):
    page.padding = 10
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def toggle_icon_button(e):
        e.control.selected = not e.control.selected
        e.control.update()

    page.add(
        ft.IconButton(
            icon=ft.Icons.BATTERY_1_BAR,
            selected_icon=ft.Icons.BATTERY_FULL,
            scale=5,
            on_click=toggle_icon_button,
            selected=False,
            style=ft.ButtonStyle(
                color={
                    ft.ControlState.SELECTED: ft.Colors.GREEN,
                    ft.ControlState.DEFAULT: ft.Colors.RED,
                }
            ),
        )
    )


ft.app(main)
