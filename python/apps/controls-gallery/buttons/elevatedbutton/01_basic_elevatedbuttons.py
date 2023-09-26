import flet as ft

name = "Basic ElevatedButtons"


def example():
    return ft.Column(
        controls=[
            ft.ElevatedButton(text="Elevated button"),
            ft.ElevatedButton("Disabled button", disabled=True),
        ]
    )


def main(page: ft.Page):
    page.title = name
    page.window_width = 390
    page.window_height = 844
    page.add(example())


if __name__ == "__main__":
    ft.app(target=main)
