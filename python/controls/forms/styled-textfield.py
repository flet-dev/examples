import flet
from flet import Page, TextField, colors


def main(page: Page):
    page.padding = 50
    page.add(
        TextField(
            text_size=30,
            cursor_color=colors.RED,
            selection_color=colors.YELLOW,
            color=colors.PINK,
            bgcolor=colors.BLACK26,
            filled=True,
            focused_color=colors.GREEN,
            focused_bgcolor=colors.CYAN_200,
            border_radius=30,
            border_color=colors.GREEN_800,
            focused_border_color=colors.GREEN_ACCENT_400,
            max_length=20,
            capitalization="characters",
        )
    )


flet.app(target=main)
