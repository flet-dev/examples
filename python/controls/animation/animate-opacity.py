import flet
from flet import ElevatedButton, Image, Page


def main(page: Page):

    c = Image(src="https://picsum.photos/200/300", opacity=None, animate_opacity=300)

    def animate_opacity(e):
        c.opacity = 0 if c.opacity == 1 else 1
        c.update()

    page.add(
        c,
        ElevatedButton(
            "Animate opacity",
            on_click=animate_opacity,
        ),
    )


flet.app(target=main)
