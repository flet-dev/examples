import flet
from flet import Dropdown, Page, colors, dropdown


def main(page: Page):
    page.padding = 50
    page.add(
        Dropdown(
            options=[
                dropdown.Option("a", "Item A"),
                dropdown.Option("b", "Item B"),
                dropdown.Option("c", "Item C"),
            ],
            border_radius=30,
            filled=True,
            border_color=colors.TRANSPARENT,
            bgcolor=colors.BLACK12,
            focused_bgcolor=colors.BLUE_100,
        )
    )


flet.app(target=main)
