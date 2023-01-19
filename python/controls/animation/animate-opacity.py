import flet as ft


def main(page: ft.Page):

    c = ft.Image(src="https://picsum.photos/200/300", opacity=None, animate_opacity=300)

    def animate_opacity(e):
        c.opacity = 0 if c.opacity == 1 else 1
        c.update()

    page.add(
        c,
        ft.ElevatedButton(
            "Animate opacity",
            on_click=animate_opacity,
        ),
    )


ft.app(target=main)
