import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Row(
            [
                ft.Image(
                    src="https://picsum.photos/300/300?1",
                    width=300,
                    height=300,
                    fit=ft.ImageFit.FILL,
                ),
                ft.ShaderMask(
                    content=ft.Image(
                        src="https://picsum.photos/300/300?1",
                        width=300,
                        height=300,
                        fit=ft.ImageFit.FILL,
                    ),
                    blend_mode=ft.BlendMode.MULTIPLY,
                    shader=ft.RadialGradient(
                        center=ft.Alignment.center(),
                        radius=0.5,
                        colors=[ft.Colors.WHITE, ft.Colors.PINK],
                        tile_mode=ft.GradientTileMode.CLAMP,
                    ),
                ),
            ]
        )
    )


ft.run(main)
