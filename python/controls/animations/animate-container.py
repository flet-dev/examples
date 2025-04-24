import flet as ft


def main(page: ft.Page):

    g1 = ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=[ft.Colors.GREEN, ft.Colors.BLUE],
        stops=[0.5, 1.0],
    )

    g2 = ft.RadialGradient(
        center=ft.alignment.top_left,
        radius=1.0,
        colors=[ft.Colors.YELLOW, ft.Colors.DEEP_ORANGE_900],
        tile_mode=ft.GradientTileMode.CLAMP,
    )
    t = ft.Text("Animate me!")
    c = ft.Container(
        t,
        width=250,
        height=250,
        gradient=g1,
        alignment=ft.alignment.top_left,
        animate=ft.animation.Animation(1000, ft.AnimationCurve.BOUNCE_OUT),
        border=ft.border.all(2, "blue"),
        border_radius=10,
        padding=10,
    )

    def animate_container(e):
        t.value = "Animate me back!" if t.value == "Animate me!" else "Animate me!"
        c.width = 150 if c.width == 250 else 250
        c.height = 150 if c.height == 250 else 250
        c.gradient = g2 if c.gradient == g1 else g1
        if c.alignment == ft.alignment.top_left:
            c.alignment = ft.alignment.bottom_right
        else:
            c.alignment = ft.alignment.top_left
        c.border_radius = 30 if c.border_radius == 10 else 10
        c.border = (
            ft.border.all(2, "black")
            if c.border == ft.border.all(2, "blue")
            else ft.border.all(2, "blue")
        )
        c.update()

    page.add(c, ft.ElevatedButton("Animate container", on_click=animate_container))


ft.app(target=main)
