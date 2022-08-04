import flet
from flet import ButtonStyle, IconButton, Page, colors, icons


def main(page: Page):
    page.padding = 50

    def toggle_icon_button(e):
        e.control.selected = not e.control.selected
        e.control.update()

    page.add(
        IconButton(
            icon=icons.BATTERY_1_BAR,
            selected_icon=icons.BATTERY_FULL,
            on_click=toggle_icon_button,
            selected=False,
            style=ButtonStyle(color={"selected": colors.GREEN, "": colors.RED}),
        )
    )


flet.app(target=main)
