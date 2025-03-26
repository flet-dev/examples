import flet
from flet import AlertDialog, ElevatedButton, OutlinedButton, Page, Text

def main(page: Page):
    page.title = "MyApp"

    def window_event(e):
        if e.data == "close":
            # Use the updated method to append the dialog to the overlay
            page.overlay.append(confirm_dialog)
            confirm_dialog.open = True
            page.update()

    page.window.prevent_close = True
    page.window.on_event = window_event

    def yes_click(e):
        # Use the updated method to destroy the window
        page.window.destroy()

    def no_click(e):
        confirm_dialog.open = False
        page.update()

    confirm_dialog = AlertDialog(
        modal=True,
        title=Text("Please confirm"),
        content=Text("Do you really want to exit this app?"),
        actions=[
            ElevatedButton("Yes", on_click=yes_click),
            OutlinedButton("No", on_click=no_click),
        ],
        actions_alignment="end",
    )

    page.add(Text('Try exiting this app by clicking window\'s "Close" button!'))

flet.app(target=main)
flet.app(target=main, view=flet.FLET_APP)
