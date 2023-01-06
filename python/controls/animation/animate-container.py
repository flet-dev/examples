import flet as ft


def main(page: ft.Page):

    g1 = ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=[ft.colors.GREEN, ft.colors.TRANSPARENT],
        stops=[0.5, 1.0],
    )

    g2 = ft.RadialGradient(
        center=ft.alignment.top_left,
        radius=1.0,
        colors=[ft.colors.YELLOW, ft.colors.DEEP_ORANGE_900],
        tile_mode=ft.GradientTileMode.CLAMP,
    )

    c = ft.Container(
        ft.Text("Animate me!"),
        width=200,
        height=200,
        bgcolor="red",
        gradient=g1,
        alignment=ft.alignment.top_left,
        animate=ft.animation.Animation(1000, ft.AnimationCurve.BOUNCE_OUT),
        border=ft.border.all(2, "blue"),
        border_radius=10,
        padding=10,
        margin=10,
    )

    def animate_container(e):
        c.width = 100 if c.width == 200 else 200
        c.height = 100 if c.height == 200 else 200
        c.bgcolor = "blue" if c.bgcolor == "red" else "red"
        c.gradient = g2 if c.gradient == g1 else g1
        if c.alignment == ft.alignment.top_left:
            c.alignment = ft.alignment.bottom_right
        else:
            c.alignment = ft.alignment.top_left
        c.border_radius = 30 if c.border_radius == 10 else 10
        c.border = ft.border.all(4, "black")
        c.padding = 50
        c.margin = 50
        c.update()

    page.add(c, ft.ElevatedButton("Animate container", on_click=animate_container))


ft.app(target=main)
