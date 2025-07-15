import flet as ft


def main(page: ft.Page):
    page.title = "Icon buttons"

    snackbar_yes = ft.SnackBar(
        content=ft.Icon(ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN_300)
    )
    snackbar_no = ft.SnackBar(
        content=ft.Icon(ft.Icons.CANCEL, color=ft.Colors.PINK_700)
    )

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(
                    icon=ft.Icons.CHECK_CIRCLE,
                    icon_color=ft.Colors.GREEN_300,
                    icon_size=40,
                    tooltip="Yep",
                    on_click=lambda e: page.show_dialog(snackbar_yes),
                ),
                ft.IconButton(
                    icon=ft.Icons.CANCEL,
                    icon_color=ft.Colors.PINK_700,
                    icon_size=40,
                    tooltip="Nope",
                    on_click=lambda e: page.show_dialog(snackbar_no),
                ),
            ],
        ),
    )


ft.run(main)
