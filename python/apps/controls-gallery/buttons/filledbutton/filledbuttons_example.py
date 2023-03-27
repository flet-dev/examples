import flet as ft

name = "FilledButtons example"

def example():
    
    return ft.Column(controls=[
        ft.FilledButton(text="Filled button"),
        ft.FilledButton("Disabled button", disabled=True),
        ft.FilledButton("Button with icon", icon="add")
    ])