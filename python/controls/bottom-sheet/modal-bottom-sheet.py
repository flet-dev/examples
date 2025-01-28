import flet as ft


def main(page: ft.Page):
    page.title = "BottomSheet example"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def bs_dismissed(e):
        page.add(ft.Text("Bottom sheet dismissed"))

    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text("Here is a bottom sheet!"),
                    ft.ElevatedButton("Dismiss", on_click=lambda _: page.close(bs)),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
            ),
            padding=50,
        ),
        open=False,
        on_dismiss=bs_dismissed,
    )
    page.overlay.append(bs)
    page.add(
        ft.ElevatedButton("Display bottom sheet", on_click=lambda e: page.open(bs))
    )


ft.app(target=main)
