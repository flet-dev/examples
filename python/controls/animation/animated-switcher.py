import flet as ft


def main(page: ft.Page):
    page.title = "AnimatedSwitcher examples"

    c1 = ft.Container(
        ft.Text("Hello!", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.Colors.GREEN,
    )
    c2 = ft.Container(
        ft.Text("Bye!", size=50),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.Colors.YELLOW,
    )
    c = ft.AnimatedSwitcher(
        c1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )

    def scale(e):
        c.content = c2 if c.content == c1 else c1
        c.transition = ft.AnimatedSwitcherTransition.SCALE
        c.update()

    def fade(e):
        c.content = c2 if c.content == c1 else c1
        c.transition = ft.AnimatedSwitcherTransition.FADE
        c.update()

    def rotate(e):
        c.content = c2 if c.content == c1 else c1
        c.transition = ft.AnimatedSwitcherTransition.ROTATION
        c.update()

    page.add(
        c,
        ft.ElevatedButton("Scale", on_click=scale),
        ft.ElevatedButton("Fade", on_click=fade),
        ft.ElevatedButton("Rotate", on_click=rotate),
    )


ft.app(main)
