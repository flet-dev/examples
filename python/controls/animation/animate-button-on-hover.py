import flet as ft


def main(page: ft.Page):
    def animate(e):
        b1.rotate = 0.1 if e.data == "true" else 0
        page.update()

    b1 = ft.ElevatedButton(
        "Hover me, I'm animated!",
        rotate=0,
        animate_rotation=100,
        on_hover=animate,
        on_click=lambda e: print("Clicked!"),
        on_long_press=lambda e: print("Long pressed!"),
    )

    page.add(b1)


ft.app(target=main)
