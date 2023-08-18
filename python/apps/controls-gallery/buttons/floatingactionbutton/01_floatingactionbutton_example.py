import flet as ft

name = "FloatingActionButton example"


def example():
    class Example(ft.Container):
        def __init__(self):
            super().__init__()
            self.content = ft.Column()

        # happens when example is added to the page (when user chooses the FloatingActionButton control from the grid)
        async def did_mount_async(self):
            self.page.floating_action_button = ft.FloatingActionButton(
                icon=ft.icons.ADD,
                bgcolor=ft.colors.LIME_300,
                data=0,
                on_click=fab_pressed,
            )
            await self.page.update_async()

        # happens when example is removed from the page (when user chooses different control group on the navigation rail)
        async def will_unmount_async(self):
            self.page.floating_action_button = None
            await self.page.update_async()

    async def fab_pressed(e):
        fab_example.content.controls.append(
            ft.ListTile(title=ft.Text(f"Tile {e.control.data}"))
        )
        await e.control.page.show_snack_bar_async(
            ft.SnackBar(ft.Text("Tile was added successfully!"), open=True)
        )
        e.control.data += 1
        await fab_example.update_async()

    fab_example = Example()

    return fab_example
