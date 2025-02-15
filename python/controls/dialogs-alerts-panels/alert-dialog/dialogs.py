import flet as ft


def main(page: ft.Page):
    page.title = "AlertDialog examples"

    dlg = ft.AlertDialog(
        title=ft.Text("Hello"),
        content=ft.Text("You are notified!"),
        alignment=ft.alignment.center,
        on_dismiss=lambda e: print("Dialog dismissed!"),
        title_padding=ft.padding.all(25),
    )

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to delete all those files?"),
        actions=[
            ft.TextButton("Yes", on_click=lambda e: page.close(dlg_modal)),
            ft.TextButton("No", on_click=lambda e: page.close(dlg_modal)),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    page.add(
        ft.ElevatedButton("Open dialog", on_click=lambda e: page.open(dlg)),
        ft.ElevatedButton("Open modal dialog", on_click=lambda e: page.open(dlg_modal)),
    )


ft.app(main)
