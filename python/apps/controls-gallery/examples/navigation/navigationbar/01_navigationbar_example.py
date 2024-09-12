import flet as ft

name = "NavigationBar Example"


def example():

    pagelet = ft.Pagelet(
        navigation_bar=ft.NavigationBar(
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
