import flet
from flet import ButtonStyle, ElevatedButton, Page, colors
from flet.border import BorderSide
from flet.buttons import RoundedRectangleBorder


def main(page: Page):
    page.padding = 50
    page.add(
        ElevatedButton(
            "Styled button 1",
            style=ButtonStyle(
                color={
                    "hovered": colors.WHITE,
                    "focused": colors.BLUE,
                    "": colors.BLACK,
                },
                bgcolor={"focused": colors.PINK_200, "": colors.YELLOW},
                padding={"hovered": 20},
                overlay_color=colors.TRANSPARENT,
                elevation={"pressed": 0, "": 1},
                animation_duration=500,
                side={
                    "": BorderSide(1, colors.BLUE),
                    "hovered": BorderSide(2, colors.BLUE),
                },
                shape={
                    "hovered": RoundedRectangleBorder(radius=20),
                    "": RoundedRectangleBorder(radius=2),
                },
            ),
        )
    )


flet.app(target=main)
