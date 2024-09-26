import flet as ft

name = "Cupertino colors"


def example():

    def copy_to_clipboard(e):
        e.control.page.set_clipboard(f"ft.colors.{e.control.content.value}")
        e.control.page.open(
            ft.SnackBar(
                ft.Text(f"Copied to clipboard: ft.colors.{e.control.content.value}"),
                open=True,
            )
        )

    cupertino_colors_column = ft.Column(spacing=0, controls=[])

    colors_list = [
        (k, v) for k, v in ft.cupertino_colors.__dict__.items() if k.isupper()
    ]

    for color in colors_list:

        if color[1] in ("activeBlue", "link"):
            text_color = ft.cupertino_colors.WHITE
        else:
            text_color = ft.cupertino_colors.ACTIVE_BLUE

        cupertino_colors_column.controls.append(
            ft.Container(
                height=50,
                bgcolor=color[1],
                content=ft.Text(color[0], color=text_color),
                alignment=ft.alignment.center,
                on_click=copy_to_clipboard,
            )
        )

    return ft.Container(border_radius=10, content=cupertino_colors_column)
