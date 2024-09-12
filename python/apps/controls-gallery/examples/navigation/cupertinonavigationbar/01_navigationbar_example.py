import flet as ft

name = "CupertinoNavigationBar Example"


def example():

    pagelet = ft.Pagelet(
        navigation_bar=ft.CupertinoNavigationBar(
            bgcolor=ft.colors.AMBER_100,
            inactive_color=ft.colors.GREY,
            active_color=ft.colors.BLACK,
            on_change=lambda e: print("Selected tab:", e.control.selected_index),
            destinations=[
                ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
                ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
                ft.NavigationBarDestination(
                    icon=ft.icons.BOOKMARK_BORDER,
                    selected_icon=ft.icons.BOOKMARK,
                    label="Explore",
                ),
            ],
        ),
        content=ft.Container(),
        height=400,
    )

    return pagelet
