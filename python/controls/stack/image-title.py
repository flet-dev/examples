import flet as ft


def main(page: ft.Page):
    st = ft.Stack(
        controls=[
            ft.Image(
                src="https://picsum.photos/300/300",
                width=300,
                height=300,
                fit=ft.BoxFit.CONTAIN,
            ),
            ft.Row(
                [
                    ft.Text(
                        "Image title",
                        color=ft.Colors.SURFACE_TINT,
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        opacity=0.5,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        width=300,
        height=300,
    )

    page.add(st)


ft.run(main)
