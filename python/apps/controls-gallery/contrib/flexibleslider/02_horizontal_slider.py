import flet as ft

name = "Horizontal slider"


def example():
    from flet_contrib.flexible_slider import FlexibleSlider

    def horizontal_slider_changed():
        print(horizontal_slider.value)

    horizontal_slider = FlexibleSlider(
        min=100,
        max=600,
        value=250,
        thickness=10,
        length=200,
        active_color=ft.colors.BLUE_500,
        inactive_color=ft.colors.YELLOW_300,
        thumb_color=ft.colors.GREEN,
        thumb_radius=20,
        on_change=horizontal_slider_changed,
    )

    return horizontal_slider
