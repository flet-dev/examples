import flet as ft

name = "Customize ScrollBar theme"


def example():

    cl = ft.Column(
        spacing=10,
        height=200,
        width=200,
        scroll=ft.ScrollMode.ALWAYS,
    )

    for i in range(0, 50):
        cl.controls.append(ft.Text(f"Text line {i}"))

    c = ft.Container(
        content=cl, 
        height=300, 
        width=300,
        border=ft.border.all(1, "black"))

    c.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            track_color={
                ft.MaterialState.HOVERED: ft.colors.AMBER,
                ft.MaterialState.DEFAULT: ft.colors.TRANSPARENT,
            },
            track_visibility=True,
            track_border_color=ft.colors.BLUE,
            thumb_visibility=True,
            thumb_color={
                ft.MaterialState.HOVERED: ft.colors.RED,
                ft.MaterialState.DEFAULT: ft.colors.GREY_300,
            },
            thickness=30,
            radius=15,
            main_axis_margin=5,
            cross_axis_margin=10,
            # interactive=False,
        )
    )

    return c