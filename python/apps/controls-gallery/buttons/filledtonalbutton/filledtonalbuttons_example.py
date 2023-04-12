import flet as ft

name = "FilledTonalButtons example"

def example():
    
    return ft.Column(controls=[
        ft.FilledTonalButton(text="FilledTonalButton"),
        ft.FilledTonalButton("Disabled button", disabled=True),
        ft.FilledTonalButton("Button with icon", icon="add")
    ])