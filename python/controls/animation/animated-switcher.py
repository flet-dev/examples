import flet
from flet import (
    AnimatedSwitcher,
    Container,
    ElevatedButton,
    Page,
    Text,
    alignment,
    colors,
)


def main(page: Page):

    c1 = Container(
        Text("Hello!", style="headlineMedium"),
        alignment=alignment.center,
        width=200,
        height=200,
        bgcolor=colors.GREEN,
    )
    c2 = Container(
        Text("Bye!", size=50),
        alignment=alignment.center,
        width=200,
        height=200,
        bgcolor=colors.YELLOW,
    )
    c = AnimatedSwitcher(
        c1,
        transition="scale",
        duration=500,
        reverse_duration=100,
        switch_in_curve="bounceOut",
        switch_out_curve="bounceIn",
    )

    def animate(e):
        c.content = c2 if c.content == c1 else c1
        c.update()

    page.add(
        c,
        ElevatedButton("Animate!", on_click=animate),
    )


flet.app(target=main)
