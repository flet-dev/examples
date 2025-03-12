import flet as ft


def main(page: ft.Page):
    page.title = "Icon buttons"

    sby = ft.SnackBar(ft.Icon(ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN_300))
    sbn = ft.SnackBar(ft.Icon(ft.Icons.CANCEL, color=ft.Colors.PINK_700))
    page.add(
        ft.Row(
            [
                ft.IconButton(
                    icon=ft.Icons.CHECK_CIRCLE,
                    icon_color=ft.Colors.GREEN_300,
                    icon_size=40,
                    tooltip="Yep",
                    on_click=lambda e: page.open(sby),
                ),
                ft.IconButton(
                    icon=ft.Icons.CANCEL,
                    icon_color=ft.Colors.PINK_700,
                    icon_size=40,
                    tooltip="Nope",
                    on_click=lambda e: page.open(sbn),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )


ft.app(main)
