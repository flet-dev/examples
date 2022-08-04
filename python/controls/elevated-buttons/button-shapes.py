import flet
from flet import ButtonStyle, FilledButton, Page
from flet.buttons import (
    BeveledRectangleBorder,
    CircleBorder,
    CountinuosRectangleBorder,
    RoundedRectangleBorder,
    StadiumBorder,
)


def main(page: Page):
    page.padding = 30
    page.spacing = 30
    page.add(
        FilledButton(
            "Stadium",
            style=ButtonStyle(
                shape=StadiumBorder(),
            ),
        ),
        FilledButton(
            "Rounded rectangle",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10),
            ),
        ),
        FilledButton(
            "Continuous rectangle",
            style=ButtonStyle(
                shape=CountinuosRectangleBorder(radius=30),
            ),
        ),
        FilledButton(
            "Beveled rectangle",
            style=ButtonStyle(
                shape=BeveledRectangleBorder(radius=10),
            ),
        ),
        FilledButton(
            "Circle",
            style=ButtonStyle(shape=CircleBorder(), padding=30),
        ),
    )


flet.app(target=main)
