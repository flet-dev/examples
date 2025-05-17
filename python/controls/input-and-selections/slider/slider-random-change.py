import asyncio
import random
import flet as ft


async def main(page):

    def slider_changed(e):
        t.value = f"Slider changed to {e.control.value}"
        page.update()

    t = ft.Text()
    s = ft.Slider(label="{value}", on_change=slider_changed)

    page.add(
        ft.Text("Slider with 'on_change' event:"),
        s,
        t,
    )

    while True:
        await asyncio.sleep(1)
        val = s.value = random.random()
        e = ft.ControlEvent("_", s, data=val)
        slider_changed(e)
        s.update()


ft.run(main)
