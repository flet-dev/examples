import flet as ft

name = "TextFields with prefixes and suffixes"

def example():
    
    return ft.Column(controls=[
                ft.TextField(label="With prefix", prefix_text="https://"),
        ft.TextField(label="With suffix", suffix_text=".com"),
        ft.TextField(
            label="With prefix and suffix", prefix_text="https://", suffix_text=".com"
        ),
        ft.TextField(
            label="My favorite color",
            icon=ft.icons.FORMAT_SIZE,
            hint_text="Type your favorite color",
            helper_text="You can type only one color",
            counter_text="0 symbols typed",
            prefix_icon=ft.icons.COLOR_LENS,
            suffix_text="...is your color",
        )
        ]
        )