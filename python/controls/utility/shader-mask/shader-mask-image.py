import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Row(
            [
                ft.ShaderMask(
                    content=ft.Image(
                        src="https://picsum.photos/200/300?1",
                        width=400,
                        height=400,
                        fit=ft.ImageFit.FILL,
                    ),
                    blend_mode=ft.BlendMode.COLOR_BURN,
                    shader=ft.RadialGradient(
                        center=ft.alignment.top_left,
                        radius=1.0,
                        colors=[ft.Colors.YELLOW, ft.Colors.DEEP_ORANGE_900],
                        tile_mode=ft.GradientTileMode.CLAMP,
                    ),
                ),
                ft.ShaderMask(
                    content=ft.Image(src="https://picsum.photos/200/300?2"),
                    blend_mode=ft.BlendMode.DST_IN,
                    shader=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[ft.Colors.BLACK, ft.Colors.TRANSPARENT],
                        stops=[0.5, 1.0],
                    ),
                ),
            ]
        )
    )


ft.run(main)
