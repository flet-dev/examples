import flet as ft


def main(page: ft.Page):

    page.add(
        ft.Stack(
            [
                ft.Container(
                    content=ft.Text("Hello"),
                    image_src="https://picsum.photos/100/100",
                    width=100,
                    height=100,
                ),
                ft.Container(
                    width=50,
                    height=50,
                    blur=10,
                    bgcolor="#44CCCC00",
                ),
                ft.Container(
                    width=50,
                    height=50,
                    left=10,
                    top=60,
                    blur=(0, 10),
                ),
                ft.Container(
                    top=10,
                    left=60,
                    blur=ft.Blur(10, 0, ft.BlurTileMode.MIRROR),
                    width=50,
                    height=50,
                    bgcolor="#44CCCCCC",
                    # border_radius=10,
                    border=ft.border.all(2, ft.colors.BLACK),
                ),
            ]
        )
    )


ft.app(main)
