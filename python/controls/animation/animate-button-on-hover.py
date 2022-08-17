import flet
from flet import ElevatedButton, Page


def main(page: Page):
    def animate(e):
        b1.rotate = 0.1 if e.data == "true" else 0
        page.update()

    b1 = ElevatedButton(
        "Hover me, I'm animated!",
        rotate=0,
        animate_rotation=100,
        on_hover=animate,
        on_click=lambda e: print("Clicked!"),
        on_long_press=lambda e: print("Long pressed!"),
    )

    page.add(b1)


flet.app(target=main)
