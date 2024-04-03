import flet as ft

name = "CupertinoDialogAction example"


def example():
    async def dismiss_dialog(e):
        cupertino_alert_dialog.open = False
        await e.control.page.update_async()

    cupertino_alert_dialog = ft.CupertinoAlertDialog(
        title=ft.Text("Cupertino Alert Dialog"),
        content=ft.Text("Do you want to delete this file?"),
        actions=[
            ft.CupertinoDialogAction(
                "OK", is_destructive_action=True, on_click=dismiss_dialog
            ),
            ft.CupertinoDialogAction(text="Cancel", on_click=dismiss_dialog),
        ],
    )

    def open_dlg(e):
        e.control.page.dialog = cupertino_alert_dialog
        cupertino_alert_dialog.open = True
        e.control.page.update()

    return ft.ElevatedButton("Open CupertinoAlertDialog", on_click=open_dlg)
