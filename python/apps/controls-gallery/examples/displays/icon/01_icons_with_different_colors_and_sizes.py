import flet as ft

name = "Icons with different colors and sizes"

def example():
    
    return ft.Row(
            [
                ft.Icon(name=ft.icons.FAVORITE, color=ft.colors.PINK),
                ft.Icon(name=ft.icons.AUDIOTRACK, color=ft.colors.GREEN_400, size=30),
                ft.Icon(name=ft.icons.BEACH_ACCESS, color=ft.colors.BLUE, size=50),
                ft.Icon(name="settings", color="#c1c1c1"),
            ]
        )