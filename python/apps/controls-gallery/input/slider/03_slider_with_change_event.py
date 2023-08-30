import flet as ft

name = "Slider with `change` event"


def example():
    async def slider_changed(e):
        t.value = f"Slider changed to {e.control.value}"
        await t.update_async()

    t = ft.Text()

    return ft.Column(
        controls=[
            ft.Text("Slider with 'on_change' event:"),
            ft.Slider(
                min=0, max=100, divisions=10, label="{value}%", on_change=slider_changed
            ),
            t,
        ]
    )
