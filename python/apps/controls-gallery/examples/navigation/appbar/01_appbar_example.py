import flet as ft

name = "AppBar Example"


def example():

    pagelet = ft.Pagelet(
        appbar=ft.AppBar(
            leading=ft.Icon(ft.icons.PALETTE),
            leading_width=40,
            title=ft.Text("AppBar Title"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
                ft.IconButton(ft.icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Item 1"),
                        ft.PopupMenuItem(),  # divider
                        ft.PopupMenuItem(
                            text="Checked item",
                            checked=False,
                        ),
                    ]
                ),
            ],
        ),
        content=ft.Container(),
    )

    return pagelet
