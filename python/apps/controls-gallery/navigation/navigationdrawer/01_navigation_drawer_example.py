import flet as ft

name = "NavigationDrawer example"


def example():
    end_drawer = ft.NavigationDrawer(
        controls=[
            ft.NavigationDrawerDestination(
                icon=ft.icons.ADD_TO_HOME_SCREEN_SHARP, label="Item 1"
            ),
            ft.NavigationDrawerDestination(icon=ft.icons.ADD_COMMENT, label="Item 2"),
        ],
    )

    drawer = ft.NavigationDrawer(
        controls=[
            ft.NavigationDrawerDestination(
                icon=ft.icons.ADD_TO_HOME_SCREEN_SHARP, label="Item 1"
            ),
            ft.NavigationDrawerDestination(icon=ft.icons.ADD_COMMENT, label="Item 2"),
        ],
    )

    async def open_end_drawer(e):
        e.control.page.end_drawer = end_drawer
        end_drawer.open = True
        await e.control.page.update_async()

    async def open_drawer(e):
        e.control.page.drawer = drawer
        drawer.open = True
        await e.control.page.update_async()

    return ft.Column(
        [
            ft.ElevatedButton("Open end drawer", on_click=open_end_drawer),
            ft.ElevatedButton("Open drawer", on_click=open_drawer),
        ]
    )
