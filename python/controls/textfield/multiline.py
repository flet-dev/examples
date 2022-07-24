import flet
from flet import Page, TextField


def main(page: Page):
    page.add(
        TextField(label="standard", multiline=True),
        TextField(
            label="disabled",
            multiline=True,
            disabled=True,
            value="line1\nline2\nline3\nline4\nline5",
        ),
        TextField(
            label="Auto adjusted height with max lines",
            multiline=True,
            min_lines=1,
            max_lines=3,
        ),
    )


flet.app(target=main)
