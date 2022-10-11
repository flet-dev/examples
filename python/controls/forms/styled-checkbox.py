import flet
from flet import Checkbox, Page


def main(page: Page):
    page.add(
        Checkbox(label="Checkbox with default style"),
        Checkbox(
            label="Checkbox with constant fill color",
            fill_color="red",
            check_color="yellow",
        ),
        Checkbox(
            label="Checkbox with dynamic fill color",
            fill_color={"hovered": "blue", "selected": "green", "": "red"},
        ),
    )


flet.app(target=main)
