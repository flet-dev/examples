import flet as ft


def main(page: ft.Page):
    page.title = "BottomSheet example"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_sheet_dismissal(e):
        page.add(ft.Text("Bottom sheet dismissed"))

    bs = ft.BottomSheet(
        open=False,
        on_dismiss=handle_sheet_dismissal,
        content=ft.Container(
            padding=50,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                controls=[
                    ft.Text("Here is a bottom sheet!"),
                    ft.ElevatedButton("Dismiss", on_click=lambda _: page.pop_dialog()),
                ],
            ),
        ),
    )
    page.overlay.append(bs)
    page.add(
        ft.ElevatedButton(
            content="Display bottom sheet",
            on_click=lambda e: page.show_dialog(bs),
        )
    )


ft.run(main)
