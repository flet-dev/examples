import flet
from flet import Page, TextField


def main(page: Page):
    page.add(
        TextField(
            label="Password with reveal button", password=True, can_reveal_password=True
        )
    )


flet.app(target=main)
