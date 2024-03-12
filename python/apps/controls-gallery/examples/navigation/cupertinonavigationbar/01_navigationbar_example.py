import flet as ft

name = "CupertinoNavigationBar Example"


def example():
    class Example(ft.Column):
        def __init__(self):
            super().__init__()
            self.cupertino_navigation_bar = ft.CupertinoNavigationBar(
                bgcolor=ft.colors.AMBER_100,
                inactive_color=ft.colors.GREY,
                active_color=ft.colors.BLACK,
                on_change=lambda e: print("Selected tab:", e.control.selected_index),
                destinations=[
                    ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore"),
                    ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Commute"),
                    ft.NavigationDestination(
                        icon=ft.icons.BOOKMARK_BORDER,
                        selected_icon=ft.icons.BOOKMARK,
                        label="Explore",
                    ),
                ],
            )

            self.controls = [
                ft.ElevatedButton(
                    "Show NavigationBar", on_click=self.show_navigation_bar
                ),
            ]

        async def show_navigation_bar(self, e):
            e.control.page.navigation_bar = self.cupertino_navigation_bar
            await e.control.page.update_async()

        # happens when example is removed from the page (when user chooses different control group on the navigation rail)
        async def will_unmount_async(self):
            self.page.navigation_bar = None
            await self.page.update_async()

    cupertino_navigation_bar_example = Example()

    return cupertino_navigation_bar_example


import flet as ft
