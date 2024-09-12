import flet as ft

name = "BottomAppBar Example"


def example():

    pagelet = ft.Pagelet(
        bottom_app_bar=ft.BottomAppBar(
            bgcolor=ft.colors.BLUE,
            shape=ft.NotchShape.CIRCULAR,
            content=ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                    ft.Container(expand=True),
                    ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                    ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
                ]
            ),
        ),
        content=ft.Container(),
        height=400,
    )

    return pagelet
