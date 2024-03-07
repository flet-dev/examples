import flet as ft

name = "TimePicker example"


def example():
    class Example(ft.Column):
        def __init__(self):
            super().__init__()
            self.timepicker = ft.TimePicker(
                confirm_text="Confirm",
                error_invalid_text="Time out of range",
                help_text="Pick your time slot",
                on_change=self.change_time,
            )
            self.selected_time = ft.Text()

            self.controls = [
                ft.ElevatedButton(
                    "Pick time",
                    icon=ft.icons.CALENDAR_MONTH,
                    on_click=self.open_time_picker,
                ),
                self.selected_time,
            ]

        async def open_time_picker(self, e):
            await self.timepicker.pick_time_async()

        async def change_time(self, e):
            self.selected_time.value = f"Selected time: {self.timepicker.value}"
            await e.control.page.update_async()

        # happens when example is added to the page (when user chooses the DatePicker control from the grid)
        def did_mount(self):
            self.page.overlay.append(self.timepicker)
            self.page.update()

        # happens when example is removed from the page (when user chooses different control group on the navigation rail)
        def will_unmount(self):
            self.page.overlay.remove(self.timepicker)
            self.page.update()

    timepicker_example = Example()

    return timepicker_example
