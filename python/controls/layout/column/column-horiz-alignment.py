import flet as ft


class ColumnFromAlignment(ft.Column):
    def __init__(self, alignment: ft.CrossAxisAlignment):
        super().__init__()
        self.controls = [
            ft.Text(str(alignment), size=16),
            ft.Container(
                bgcolor=ft.Colors.AMBER_100,
                width=100,
                content=ft.Column(
                    controls=self.get_items(3),
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=alignment,
                ),
            ),
        ]

    @staticmethod
    def get_items(count):
        return [
            ft.Container(
                content=ft.Text(value=str(i)),
                alignment=ft.Alignment.CENTER,
                width=50,
                height=50,
                bgcolor=ft.Colors.AMBER_500,
            )
            for i in range(1, count + 1)
        ]


def main(page: ft.Page):
    page.add(
        ft.Row(
            spacing=30,
            alignment=ft.MainAxisAlignment.START,
            controls=[
                ColumnFromAlignment(ft.CrossAxisAlignment.START),
                ColumnFromAlignment(ft.CrossAxisAlignment.CENTER),
                ColumnFromAlignment(ft.CrossAxisAlignment.END),
            ],
        )
    )


ft.run(main)
