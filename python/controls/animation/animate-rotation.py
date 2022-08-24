import flet
from flet import Container, ElevatedButton, Page, Stack, alignment, animation, transform


def main(page: Page):

    c1 = Container(
        width=140,
        height=100,
        left=200,
        top=100,
        bgcolor="red",
        border_radius=5,
        rotate=1,
        animate_rotation=1000,
    )

    c2 = Container(
        width=100,
        height=70,
        bgcolor="blue",
        border_radius=5,
        rotate=transform.Rotate(-1, alignment=alignment.center_left),
        animate_rotation=animation.Animation(duration=300),
    )

    def animate(e):
        c1.rotate += 1
        c2.rotate.angle -= 1
        page.update()

    page.add(
        Stack([c1, c2], width=600, height=600),
        ElevatedButton("Animate!", on_click=animate),
    )


flet.app(target=main)
