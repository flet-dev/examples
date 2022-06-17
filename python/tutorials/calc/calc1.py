import flet
from flet import ElevatedButton, Page, Text


def main(page: Page):
    page.title = "Calc App"
    result = Text(value="0")

    page.add(
        result,
        ElevatedButton(text="AC"),
        ElevatedButton(text="+/-"),
        ElevatedButton(text="%"),
        ElevatedButton(text="/"),
        ElevatedButton(text="7"),
        ElevatedButton(text="8"),
        ElevatedButton(text="9"),
        ElevatedButton(text="*"),
        ElevatedButton(text="4"),
        ElevatedButton(text="5"),
        ElevatedButton(text="6"),
        ElevatedButton(text="-"),
        ElevatedButton(text="1"),
        ElevatedButton(text="2"),
        ElevatedButton(text="3"),
        ElevatedButton(text="+"),
        ElevatedButton(text="0"),
        ElevatedButton(text="."),
        ElevatedButton(text="="),
    )


flet.app(target=main)
