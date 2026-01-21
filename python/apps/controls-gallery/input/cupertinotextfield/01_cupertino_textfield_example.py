import flet as ft

name = "CupertinoTextField example"


def example():
    t1 = ft.CupertinoTextField(
            placeholder_text="Enter text here",
        )

    t2 = ft.CupertinoTextField(
            bgcolor=ft.colors.BLUE_100,
            shadow=ft.BoxShadow(color=ft.colors.RED_400, blur_radius=5, spread_radius=5),
            placeholder_text="Enter text here",
            placeholder_style=ft.TextStyle(color=ft.colors.GREEN_300, italic=True),
            suffix=ft.Icon(ft.icons.EDIT),
            suffix_visibility_mode=ft.VisibilityMode.EDITING,
        )

    return ft.Column(controls=[t1, t2])
