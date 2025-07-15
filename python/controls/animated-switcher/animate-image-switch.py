import time

import flet as ft


def main(page: ft.Page):
    i = ft.Image(src="https://picsum.photos/200/300", width=200, height=300)

    def animate(e):
        switcher.content = ft.Image(
            src=f"https://picsum.photos/200/300?{time.time()}", width=200, height=300
        )
        page.update()

    switcher = ft.AnimatedSwitcher(
        content=i,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )

    page.add(
        switcher,
        ft.ElevatedButton("Animate!", on_click=animate),
    )


ft.run(main)
