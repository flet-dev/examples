import flet as ft

name = "Simple BottomSheet"


def example():
    class Example(ft.ElevatedButton):
        def __init__(self):
            super().__init__()
            self.text = "Display bottom sheet"
            self.on_click = self.show_bs
            self.bs = ft.BottomSheet(
                ft.Container(
                    ft.Column(
                        [
                            ft.Text("This is sheet's content!"),
                            ft.ElevatedButton(
                                "Close bottom sheet", on_click=self.close_bs
                            ),
                        ],
                        tight=True,
                    ),
                    padding=10,
                ),
                open=False,
                on_dismiss=self.bs_dismissed,
            )

        def bs_dismissed(self, e):
            print("Dismissed!")

        async def show_bs(self, e):
            self.bs.open = True
            await self.bs.update_async()

        async def close_bs(self, e):
            self.bs.open = False
            await self.bs.update_async()

        # happens when example is added to the page (when user chooses the BottomSheet control from the grid)
        async def did_mount_async(self):
            self.page.overlay.append(self.bs)
            await self.page.update_async()

        # happens when example is removed from the page (when user chooses different control group on the navigation rail)
        async def will_unmount_async(self):
            self.page.overlay.remove(self.bs)
            await self.page.update_async()

    bs_example = Example()

    return bs_example
