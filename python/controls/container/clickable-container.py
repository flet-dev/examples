import flet
from flet import Container, Page, Row, Text, alignment, colors


def main(page: Page):
    page.title = "Containers - clickable and not"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    page.add(
        Row(
            [
                Container(
                    content=Text("Non clickable"),
                    margin=10,
                    padding=10,
                    alignment=alignment.center,
                    bgcolor=colors.AMBER,
                    width=150,
                    height=150,
                    border_radius=10,
                ),
                Container(
                    content=Text("Clickable without Ink"),
                    margin=10,
                    padding=10,
                    alignment=alignment.center,
                    bgcolor=colors.GREEN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    on_click=lambda e: print("Clickable without Ink clicked!"),
                ),
                Container(
                    content=Text("Clickable with Ink"),
                    margin=10,
                    padding=10,
                    alignment=alignment.center,
                    bgcolor=colors.CYAN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable with Ink clicked!"),
                ),
                Container(
                    content=Text("Clickable transparent with Ink"),
                    margin=10,
                    padding=10,
                    alignment=alignment.center,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable transparent with Ink clicked!"),
                ),
            ],
            alignment="center",
        ),
    )


flet.app(target=main)
