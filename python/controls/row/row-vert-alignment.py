import flet as ft


def main(page: ft.Page):
    def items(count):
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    content=ft.Text(value=str(i)),
                    alignment=ft.alignment.center,
                    width=50,
                    height=50,
                    bgcolor=ft.colors.AMBER_500,
                )
            )
        return items

    def row_with_vertical_alignment(align: ft.CrossAxisAlignment):
        return ft.Column(
            [
                ft.Text(str(align), size=16),
                ft.Container(
                    content=ft.Row(items(3), vertical_alignment=align),
                    bgcolor=ft.colors.AMBER_100,
                    height=150,
                ),
            ]
        )

    page.add(
        row_with_vertical_alignment(ft.CrossAxisAlignment.START),
        row_with_vertical_alignment(ft.CrossAxisAlignment.CENTER),
        row_with_vertical_alignment(ft.CrossAxisAlignment.END),
    )


ft.app(target=main)
