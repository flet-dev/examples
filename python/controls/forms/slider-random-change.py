import time
import random
import flet as ft


def main(page):

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
        time.sleep(1)
        val = s.value = random.random()
        e = ft.ControlEvent("_", "_", "_", s, val)
        slider_changed(e)
        s.update()


ft.app(main)
