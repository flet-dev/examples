import flet as ft

name = "Gradually fade out image to the bottom edge"

def example():
    
    return ft.Row(
            [
                ft.ShaderMask(
                    ft.Image(src="https://picsum.photos/100/200?2"),
                    blend_mode=ft.BlendMode.DST_IN,
                    shader=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[ft.colors.BLACK, ft.colors.TRANSPARENT],
                        stops=[0.5, 1.0],
                    ),
                    border_radius=10,
                ),
            ]
        )