import flet as ft

name = "Adding a pink glow around image edges"

def example():
    
    return ft.Row(
            [
                ft.ShaderMask(
                    ft.Image(
                        src="https://picsum.photos/200/200?1",
                        width=200,
                        height=200,
                        fit=ft.ImageFit.FILL,
                    ),
                    blend_mode=ft.BlendMode.MULTIPLY,
                    shader=ft.RadialGradient(
                        center=ft.alignment.center,
                        radius=2.0,
                        colors=[ft.colors.WHITE, ft.colors.PINK],
                        tile_mode=ft.GradientTileMode.CLAMP,
                    ),
                )
            ]
        )