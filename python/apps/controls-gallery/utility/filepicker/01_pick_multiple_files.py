import flet as ft

name = "Pick multiple files"


def example():
    class Example(ft.Row):
        def __init__(self):
            super().__init__()
            self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
            self.selected_files = ft.Text()

            async def pick_files(_):
                await self.pick_files_dialog.pick_files_async(allow_multiple=True)

            self.controls = [
                ft.ElevatedButton(
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=pick_files,
                ),
                self.selected_files,
            ]

        async def pick_files_result(self, e: ft.FilePickerResultEvent):
            self.selected_files.value = (
                ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
            )
            await self.selected_files.update_async()

        # happens when example is added to the page (when user chooses the FilePicker control from the grid)
        async def did_mount_async(self):
            self.page.overlay.append(self.pick_files_dialog)
            await self.page.update_async()

        # happens when example is removed from the page (when user chooses different control group on the navigation rail)
        async def will_unmount_async(self):
            self.page.overlay.remove(self.pick_files_dialog)
            await self.page.update_async()

    filepicker_example = Example()

    return filepicker_example
