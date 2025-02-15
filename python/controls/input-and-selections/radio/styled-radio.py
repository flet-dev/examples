import flet
from flet import Column, Page, Radio, RadioGroup


def main(page: Page):
    page.add(
        RadioGroup(
            Column(
                [
                    Radio(label="Radio with default style", value="1"),
                    Radio(
                        label="Radio with constant fill color",
                        value="2",
                        fill_color="red",
                    ),
                    Radio(
                        label="Radio with dynamic fill color",
                        value="3",
                        fill_color={"hovered": "blue", "selected": "green", "": "red"},
                    ),
                ]
            )
        )
    )


flet.app(target=main)
