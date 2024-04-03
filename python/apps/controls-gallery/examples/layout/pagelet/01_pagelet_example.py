import flet as ft

name = "CupertinoListTile example"


def example():
    def open_pagelet_end_drawer(e):
        pagelet.end_drawer.open = True
        pagelet.end_drawer.update()

    pagelet = ft.Pagelet(
        appbar=ft.AppBar(
            title=ft.Text("Pagelet AppBar title"), bgcolor=ft.colors.AMBER_ACCENT
        ),
        content=ft.Text("Pagelet body"),
        bgcolor=ft.colors.AMBER_100,
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
        end_drawer=ft.NavigationDrawer(
            controls=[
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_TO_HOME_SCREEN_SHARP, label="Item 1"
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_COMMENT, label="Item 2"
                ),
            ],
        ),
        floating_action_button=ft.FloatingActionButton(
            "Open", on_click=open_pagelet_end_drawer
        ),
        floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_DOCKED,
        # width=400,
        height=400,
    )

    return pagelet
