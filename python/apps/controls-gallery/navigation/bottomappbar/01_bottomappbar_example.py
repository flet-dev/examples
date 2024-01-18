import flet as ft

name = "BottomAppBar Example"


def example():
    class Example(ft.Column):
        def __init__(self):
            super().__init__()
            self.bottom_app_bar = ft.BottomAppBar(
                bgcolor=ft.colors.BLUE,
                shape=ft.NotchShape.CIRCULAR,
                content=ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                        ft.Container(expand=True),
                        ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                        ft.IconButton(
                            icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE
                        ),
                    ]
                ),
            )

            self.controls = [
                ft.ElevatedButton(
                    "Show BottomAppBar", on_click=self.show_bottom_app_bar
                ),
            ]

        async def show_bottom_app_bar(self, e):
            e.control.page.bottom_appbar = self.bottom_app_bar
            await e.control.page.update_async()

        # happens when example is removed from the page (when user chooses different control group on the navigation rail)
        async def will_unmount_async(self):
            self.page.bottom_appbar = None
            await self.page.update_async()

    bottom_app_bar_example = Example()

    return bottom_app_bar_example
