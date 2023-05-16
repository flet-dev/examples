import flet as ft

name = "Customize Theme colors"

def example():
    
    def set_primary_color(e):
        e.control.page.theme = ft.Theme(color_scheme=ft.ColorScheme(
            primary=ft.colors.GREEN,
            ),
        )
        e.control.page.update()
    
    return ft.FilledButton("Set Primary Color to GREEN", on_click=set_primary_color)