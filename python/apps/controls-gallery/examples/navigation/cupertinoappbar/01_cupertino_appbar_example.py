import flet as ft

name = "CupertinoAppBar Example"


def example():

    pagelet = ft.Pagelet(
        appbar=ft.CupertinoAppBar(
            leading=ft.Icon(ft.icons.PALETTE),
            bgcolor=ft.colors.SURFACE_VARIANT,
            trailing=ft.Icon(ft.icons.WB_SUNNY_OUTLINED),
            middle=ft.Text("CupertinoAppBar Middle"),
        ),
        content=ft.Container(),
    )

    return pagelet
