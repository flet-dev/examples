import flet as ft

name = "Basic and modal dialogs"


def example():
    dlg = ft.AlertDialog(
        title=ft.Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    async def close_dlg(e):
        dlg_modal.open = False
        await e.control.page.update_async()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to delete all those files?"),
        actions=[
            ft.TextButton("Yes", on_click=close_dlg),
            ft.TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    async def open_dlg(e):
        e.control.page.dialog = dlg
        dlg.open = True
        await e.control.page.update_async()

    async def open_dlg_modal(e):
        e.control.page.dialog = dlg_modal
        dlg_modal.open = True
        await e.control.page.update_async()

    return ft.Column(
        [
            ft.ElevatedButton("Open dialog", on_click=open_dlg),
            ft.ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
        ]
    )
