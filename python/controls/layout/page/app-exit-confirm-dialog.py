import flet as ft


def main(page: ft.Page):
    page.title = "MyApp"

    def window_event(e):
        if e.type == ft.WindowEventType.CLOSE:
            page.show_dialog(confirm_dialog)
            page.update()

    page.window.prevent_close = True
    page.window.on_event = window_event

    def yes_click(e):
        page.window.destroy()

    def no_click(e):
        page.pop_dialog()
        page.update()

    confirm_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to exit this app?"),
        actions=[
            ft.ElevatedButton(content="Yes", on_click=yes_click),
            ft.OutlinedButton(content="No", on_click=no_click),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.add(ft.Text('Try exiting this app by clicking window\'s "Close" button!'))


ft.run(main)
