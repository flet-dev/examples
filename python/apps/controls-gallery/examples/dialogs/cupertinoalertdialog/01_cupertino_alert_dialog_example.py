import flet as ft

name = "CupertinoAlertDialog example"


def example():
    def dismiss_dialog(e):
        cupertino_alert_dialog.open = False
        e.control.page.update()

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
        e.control.page.overlay.append(cupertino_alert_dialog)
        cupertino_alert_dialog.open = True
        e.control.page.update()

    return ft.ElevatedButton("Open CupertinoAlertDialog", on_click=open_dlg)
