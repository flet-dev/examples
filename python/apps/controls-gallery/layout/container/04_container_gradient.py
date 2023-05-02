import flet as ft

name = "Containers with different gradient backgrounds"

def example():

    import math

    container_1 = ft.Container(
        content=ft.Text("LinearGradient"),
        alignment=ft.alignment.center,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.colors.BLUE, ft.colors.YELLOW],
        ),
        width=150,
        height=150,
        border_radius=5,
    )

    container_2 = ft.Container(
        content=ft.Text("RadialGradient"),
        alignment=ft.alignment.center,
        gradient=ft.RadialGradient(
            colors=[ft.colors.YELLOW, ft.colors.BLUE],
        ),
        width=150,
        height=150,
        border_radius=5,
    )

    container_3 = ft.Container(
        content=ft.Text("SweepGradient"),
        alignment=ft.alignment.center,
        gradient=ft.SweepGradient(
            center=ft.alignment.center,
            start_angle=0.0,
            end_angle=math.pi * 2,
            colors=[ft.colors.YELLOW, ft.colors.BLUE],
        ),
        width=150,
        height=150,
        border_radius=5,
    )

    return ft.Row(controls=[
        container_1,
        container_2,
        container_3
        ]
    )