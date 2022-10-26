import flet
from flet import Page, Slider, Text, Theme


def main(page: Page):
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }

    t = Text(
        "This is rendered with Roboto Slab",
        size=30,
        font_family="RobotoSlab",
        weight="w100",
    )

    def width_changed(e):
        t.weight = f"w{int(e.control.value)}"
        t.update()

    page.add(
        t,
        Slider(
            min=100,
            max=900,
            divisions=8,
            label="{value}",
            width=500,
            on_change=width_changed,
        ),
    )


flet.app(target=main)
