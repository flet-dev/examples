import flet as ft

name = "Vertical slider"


def example():
    from flet_contrib.flexible_slider import FlexibleSlider

    def vertical_slider_changed():
        print(vertical_slider.value)

    vertical_slider = FlexibleSlider(
        vertical=True,
        divisions=5,
        on_change=vertical_slider_changed,
    )

    return vertical_slider
