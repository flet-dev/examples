import flet as ft

name = "IconButton with `click` event"


def example():
    async def button_clicked(e):
        b.data += 1
        t.value = f"Button clicked {b.data} time(s)"
        await t.update_async()

    b = ft.IconButton(
        icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=button_clicked, data=0
    )
    t = ft.Text()

    return ft.Column([b, t])
