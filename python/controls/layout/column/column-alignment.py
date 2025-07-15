import flet as ft


class ColumnFromAlignment(ft.Column):
    def __init__(self, alignment: ft.MainAxisAlignment):
        super().__init__()
        self.controls = [
            ft.Text(str(alignment), size=10),
            ft.Container(
                content=ft.Column(self.get_items(3), alignment=alignment),
                bgcolor=ft.Colors.AMBER_100,
                height=400,
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
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ColumnFromAlignment(ft.MainAxisAlignment.START),
                ColumnFromAlignment(ft.MainAxisAlignment.CENTER),
                ColumnFromAlignment(ft.MainAxisAlignment.END),
                ColumnFromAlignment(ft.MainAxisAlignment.SPACE_BETWEEN),
                ColumnFromAlignment(ft.MainAxisAlignment.SPACE_AROUND),
                ColumnFromAlignment(ft.MainAxisAlignment.SPACE_EVENLY),
            ],
        )
    )


ft.run(main)
