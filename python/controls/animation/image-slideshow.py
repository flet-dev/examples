import flet
from flet import ElevatedButton, Image, Page, Stack, animation


def main(page: Page):

    i1 = Image(
        src="https://picsum.photos/200/300?1",
        animate_position=animation.Animation(300, "bounceOut"),
    )
    i2 = Image(
        src="https://picsum.photos/200/300?2",
        animate_position=animation.Animation(300, "bounceOut"),
        left=-400,
    )

    def animate(e):
        i1.left = 400
        i2.left = 0
        page.update()

    page.add(
        Stack(
            [
                i1,
                i2,
            ],
            width=200,
            height=300,
        ),
        ElevatedButton("Slide!", on_click=animate),
    )


flet.app(target=main)
