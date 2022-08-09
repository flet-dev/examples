import flet
from flet import ElevatedButton, Image, Page, animation, transform


def main(page: Page):

    c = Image(
        src="https://picsum.photos/200/300?1",
        width=200,
        height=300,
        offset=transform.Offset(-2, 0),
        animate_offset=animation.Animation(300, "bounceOut"),
    )

    def animate(e):
        c.offset = transform.Offset(0, 0)
        c.update()

    page.add(
        c,
        ElevatedButton("Reveal the image!", on_click=animate),
    )


flet.app(target=main)
