import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Row(
            [
                ft.ShaderMask(
                    content=ft.Image(src="https://picsum.photos/200/200?2"),
                    blend_mode=ft.BlendMode.DST_IN,
                    shader=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[ft.Colors.BLACK, ft.Colors.TRANSPARENT],
                        stops=[0.5, 1.0],
                    ),
                    border_radius=10,
                ),
            ]
        )
    )


ft.run(main)
