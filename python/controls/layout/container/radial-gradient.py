import flet as ft


def main(page: ft.Page):

    page.add(
        ft.Container(
            alignment=ft.Alignment.center(),
            gradient=ft.RadialGradient(
                center=ft.Alignment(0.7, -0.6),
                radius=0.2,
                colors=[
                    "0xFFFFFF00",  # yellow sun
                    "0xFF0099FF",  # blue sky
                ],
                stops=[0.4, 1.0],
            ),
            width=150,
            height=150,
            border_radius=5,
        )
    )


ft.run(main)
