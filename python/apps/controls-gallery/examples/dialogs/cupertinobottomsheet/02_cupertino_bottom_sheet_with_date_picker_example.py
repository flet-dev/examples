import flet as ft

name = "CupertinoBottomSheet with CupertinoDatePicker Example"


def example():

    return ft.OutlinedButton(
        "Show CupertinoDatePicker",
        on_click=lambda e: e.control.page.open(
            ft.CupertinoBottomSheet(
                ft.CupertinoDatePicker(
                    on_change=lambda e: print(e.data),
                    date_picker_mode=ft.CupertinoDatePickerMode.DATE_AND_TIME,
                ),
                height=216,
                bgcolor=ft.CupertinoColors.SYSTEM_BACKGROUND,
                padding=ft.padding.only(top=6),
            )
        ),
    )
