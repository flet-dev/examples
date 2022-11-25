import flet as ft


def main(page: ft.Page):

    c = ft.Image(
        src="icons/icon-192.png",
        width=100,
        height=100,
        scale=1.0,
        animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE_IN_QUINT),
        opacity=1.0,
        animate_opacity=ft.animation.Animation(300, ft.AnimationCurve.EASE_IN_QUINT),
    )

    def animate(e):
        c.scale = 30
        c.opacity = 0
        c.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Column(
            [c, ft.ElevatedButton("Boom!", on_click=animate)],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


ft.app(target=main)
