import flet
from flet import Container, Page, ProgressRing, Stack, Text, alignment

def main(page: Page):

    page.add(
        Stack(
            [
                Container(Text("60%"), alignment=alignment.center),
                ProgressRing(
                    value=0.6,
                    width=100,
                    height=100,
                ),
            ],
            width=100,
            height=100,
        )
    )

flet.app(target=main)
