import flet
from flet import Page, TextField


def main(page: Page):
    page.add(
        TextField(label="Underlined", border="underline", hint_text="Enter text here"),
        TextField(
            label="Underlined filled",
            border="underline",
            filled=True,
            hint_text="Enter text here",
        ),
        TextField(label="Borderless", border="none", hint_text="Enter text here"),
        TextField(
            label="Borderless filled",
            border="none",
            filled=True,
            hint_text="Enter text here",
        ),
    )


flet.app(target=main)
