import flet as ft

name = "CupertinoDatePicker example"


def example():

    return ft.OutlinedButton(
        "Show CupertinoDatePicker",
        on_click=lambda e: e.control.page.show_bottom_sheet(
            ft.CupertinoBottomSheet(
                ft.CupertinoDatePicker(
                    on_change=lambda e: print(e.data),
                    date_picker_mode=ft.CupertinoDatePickerMode.DATE_AND_TIME,
                ),
                height=216,
                bgcolor=ft.cupertino_colors.SYSTEM_BACKGROUND,
                padding=ft.padding.only(top=6),
            )
        ),
    )
