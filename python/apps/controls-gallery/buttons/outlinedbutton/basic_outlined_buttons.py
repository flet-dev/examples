import flet as ft

name = "Basic OutlinedButtons"

def example():
    
    return ft.Column(
            [
                ft.OutlinedButton(text="Outlined button"),
                ft.OutlinedButton("Disabled button", disabled=True)
            ]
        )