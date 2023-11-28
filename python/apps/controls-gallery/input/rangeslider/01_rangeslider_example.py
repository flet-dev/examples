import flet as ft

name = "Range slider with divisions and labels"


def example():
    range_slider = ft.RangeSlider(
        min=0,
        max=50,
        start_value=10,
        divisions=10,
        end_value=20,
        label="{value}%",
    )

    return ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(height=30),
            range_slider,
        ],
    )
