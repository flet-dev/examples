import flet
from flet import (
    Container,
    ElevatedButton,
    LinearGradient,
    Page,
    RadialGradient,
    Text,
    alignment,
    animation,
    border,
    colors,
)


def main(page: Page):

    g1 = LinearGradient(
        begin=alignment.top_center,
        end=alignment.bottom_center,
        colors=[colors.GREEN, colors.TRANSPARENT],
        stops=[0.5, 1.0],
    )

    g2 = RadialGradient(
        center=alignment.top_left,
        radius=1.0,
        colors=[colors.YELLOW, colors.DEEP_ORANGE_900],
        tile_mode="clamp",
    )

    c = Container(
        Text("Animate me!"),
        width=200,
        height=200,
        bgcolor="red",
        gradient=g1,
        alignment=alignment.top_left,
        animate=animation.Animation(1000, "bounceOut"),
        border=border.all(2, "blue"),
        border_radius=10,
        padding=10,
        margin=10,
    )

    def animate_container(e):
        c.width = 100 if c.width == 200 else 200
        c.height = 100 if c.height == 200 else 200
        c.bgcolor = "blue" if c.bgcolor == "red" else "red"
        c.gradient = g2 if c.gradient == g1 else g1
        if c.alignment == alignment.top_left:
            c.alignment = alignment.bottom_right
        else:
            c.alignment = alignment.top_left
        c.border_radius = 30 if c.border_radius == 10 else 10
        c.border = border.all(4, "black")
        c.padding = 50
        c.margin = 50
        c.update()

    page.add(c, ElevatedButton("Animate container", on_click=animate_container))


flet.app(target=main)
