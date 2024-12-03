import flet as ft

name = """Checkbox with different label_style properties"""


def example():

    checkbox = ft.Checkbox(
        label="Checkbox label",
        label_style=ft.TextStyle(size=20, height=20, weight=5),
    )

    return ft.Column(
        [
            checkbox,
        ]
    )
