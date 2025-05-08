import flet as ft


def main(page: ft.Page):
    page.title = "Elevated buttons with custom content"
    page.add(
        ft.ElevatedButton(
            width=150,
            content=ft.Row(
                [
                    ft.Icon(name=ft.Icons.FAVORITE, color=ft.Colors.PINK),
                    ft.Icon(name=ft.Icons.AUDIOTRACK, color=ft.Colors.GREEN),
                    ft.Icon(name=ft.Icons.BEACH_ACCESS, color=ft.Colors.BLUE),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
        ),
        ft.ElevatedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value="Compound button", size=20),
                        ft.Text(value="This is secondary text"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=ft.Padding.all(10),
            ),
        ),
    )


ft.run(main)
