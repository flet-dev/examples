import flet as ft

name = "TextField with `change` event"


def example():
    async def textbox_changed(e):
        t.value = e.control.value
        await t.update_async()

    t = ft.Text()
    tb = ft.TextField(
        label="TextField with 'change' event:",
        on_change=textbox_changed,
    )

    return ft.Column(controls=[tb, t])
