import flet as ft

name = "OutlinedButtons with icons"

def example():
    
    return ft.Column(
            [
                ft.OutlinedButton("Button with icon", icon="chair_outlined"),
                ft.OutlinedButton(
                    "Button with colorful icon",
                    icon="park_rounded",
                    icon_color="green400",
                )
            ]
        )