import flet as ft

name = "ElevatedButton with 'click' event"


def example():
    async def button_clicked(e):
        b.data += 1
        t.value = f"Button clicked {b.data} time(s)"
        await t.update_async()

    b = ft.ElevatedButton("Button with 'click' event", on_click=button_clicked, data=0)
    t = ft.Text()

    return ft.Column(controls=[b, t])
