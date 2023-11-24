import flet as ft
import datetime

name = "DatePicker example"


def example():
    class Example(ft.Column):
        def __init__(self):
            super().__init__()
            self.datepicker = ft.DatePicker(
                first_date=datetime.datetime(2023, 10, 1),
                last_date=datetime.datetime(2024, 10, 1),
            )

            async def open_date_picker(e):
                await self.datepicker.pick_date_async()
                # await e.control.page.update_async()

            self.controls = [
                ft.ElevatedButton(
                    "Pick date",
                    icon=ft.icons.CALENDAR_MONTH,
                    on_click=open_date_picker,
                ),
            ]

        # happens when example is added to the page (when user chooses the DatePicker control from the grid)
        async def did_mount_async(self):
            self.page.overlay.append(self.datepicker)
            await self.page.update_async()

        # happens when example is removed from the page (when user chooses different control group on the navigation rail)
        async def will_unmount_async(self):
            self.page.overlay.remove(self.datepicker)
            await self.page.update_async()

    datepicker_example = Example()

    return datepicker_example
