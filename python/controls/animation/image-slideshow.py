import flet as ft


def main(page: ft.Page):

    i1 = ft.Image(
        src="https://picsum.photos/200/300?1",
        animate_position=ft.animation.Animation(300, ft.AnimationCurve.BOUNCE_OUT),
    )
    i2 = ft.Image(
        src="https://picsum.photos/200/300?2",
        animate_position=ft.animation.Animation(300, ft.AnimationCurve.BOUNCE_OUT),
        left=-400,
    )

    def animate(e):
        i1.left = 400
        i2.left = 0
        page.update()

    page.add(
        ft.Stack(
            [
                i1,
                i2,
            ],
            width=200,
            height=300,
        ),
        ft.ElevatedButton("Slide!", on_click=animate),
    )


ft.app(target=main)
