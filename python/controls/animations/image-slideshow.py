import flet as ft


def main(page: ft.Page):

    i1 = ft.Image(
        src="https://picsum.photos/200/300?1",
        animate_position=ft.Animation(300, ft.AnimationCurve.BOUNCE_OUT),
        left=0,
    )
    i2 = ft.Image(
        src="https://picsum.photos/200/300?2",
        animate_position=ft.Animation(300, ft.AnimationCurve.BOUNCE_OUT),
        left=-400,
    )

    def animate(e):
        i1.left = 400 if i1.left == 0 else 0
        i2.left = 0 if i2.left == -400 else -400
        page.update()

    page.add(
        ft.Stack(
            [i1, i2],
            width=200,
            height=300,
        ),
        ft.ElevatedButton("Slide!", on_click=animate),
    )


ft.app(main)
