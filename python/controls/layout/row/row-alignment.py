import flet as ft


def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO

    def items(count):
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    content=ft.Text(value=str(i)),
                    alignment=ft.alignment.center,
                    width=50,
                    height=50,
                    bgcolor=ft.Colors.AMBER_500,
                )
            )
        return items

    def row_with_alignment(align: ft.MainAxisAlignment):
        return ft.Column(
            [
                ft.Text(str(align), size=16),
                ft.Container(
                    content=ft.Row(items(3), alignment=align),
                    bgcolor=ft.Colors.AMBER_100,
                ),
            ],
        )

    page.add(
        ft.Column(
            [
                row_with_alignment(ft.MainAxisAlignment.START),
                row_with_alignment(ft.MainAxisAlignment.CENTER),
                row_with_alignment(ft.MainAxisAlignment.END),
                row_with_alignment(ft.MainAxisAlignment.SPACE_BETWEEN),
                row_with_alignment(ft.MainAxisAlignment.SPACE_AROUND),
                row_with_alignment(ft.MainAxisAlignment.SPACE_EVENLY),
            ],
            scroll=ft.ScrollMode.AUTO,
        )
    )


ft.app(main)
