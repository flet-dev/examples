import flet
from flet import BottomSheet, Column, Container, ElevatedButton, Page, Text


def main(page: Page):
    def bs_dismissed(e):
        print("Dismissed!")

    def show_bs(e):
        bs.open = True
        bs.update()

    def close_bs(e):
        bs.open = False
        bs.update()

    bs = BottomSheet(
        Container(
            Column(
                [
                    Text("This is content!"),
                    ElevatedButton("Close bottom sheet", on_click=close_bs),
                ],
                tight=True,
            ),
            padding=10,
        ),
        open=True,
        on_dismiss=bs_dismissed,
    )
    page.overlay.append(bs)
    page.add(ElevatedButton("Display bottom sheet", on_click=show_bs))


flet.app(target=main)
