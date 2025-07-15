import flet as ft


def main(page: ft.Page):

    c1 = ft.ShaderMask(
        blend_mode=ft.BlendMode.COLOR_BURN,
        border_radius=5,
        animate_rotation=300,
        animate_scale=ft.Animation(600, ft.AnimationCurve.BOUNCE_OUT),
        shader=ft.RadialGradient(
            center=ft.Alignment.TOP_LEFT,
            radius=1.0,
            colors=[ft.Colors.YELLOW, ft.Colors.DEEP_ORANGE_900],
            tile_mode=ft.GradientTileMode.CLAMP,
        ),
        content=ft.Image(
            src="https://picsum.photos/140/100?1",
            width=140,
            height=100,
            fit=ft.BoxFit.FILL,
        ),
    )

    def animate(e):
        c1.rotate = 1
        c1.scale = 3
        page.update()

    page.add(
        ft.Stack([c1], width=500, height=300),
        ft.ElevatedButton("Animate!", on_click=animate),
    )


ft.run(main)
