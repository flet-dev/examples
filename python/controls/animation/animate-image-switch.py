import time

import flet as ft


def main(page: ft.Page):

    i = ft.Image(src="https://picsum.photos/200/300", width=200, height=300)

    def animate(e):
        sw.content = ft.Image(
            src=f"https://picsum.photos/200/300?{time.time()}", width=200, height=300
        )
        page.update()

    sw = ft.AnimatedSwitcher(
        i,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )

    page.add(
        sw,
        ft.ElevatedButton("Animate!", on_click=animate),
    )


ft.app(target=main)
