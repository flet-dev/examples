import flet as ft

name = """Checkbox with different properties"""


def example():

    checkbox = ft.Checkbox(
        label="Checkbox label",
        value=True,
        label_position=ft.LabelPosition.LEFT,
        label_style=ft.TextStyle(size=10),
    )

    return ft.Column(
        [
            checkbox,
        ]
    )
