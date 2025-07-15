import asyncio
import random
import flet as ft


async def main(page: ft.Page):
    def slider_changed(e: ft.Event[ft.Slider]):
        message.value = f"Slider changed to {e.control.value}"
        message.update()

    page.add(
        ft.Text("Slider with 'on_change' event:"),
        slider := ft.Slider(label="{value}", on_change=slider_changed),
        message := ft.Text(),
    )

    while True:
        await asyncio.sleep(1)
        val = slider.value = random.random()
        event = ft.ControlEvent("_", slider, data=val)
        slider_changed(event)
        slider.update()


ft.run(main)
