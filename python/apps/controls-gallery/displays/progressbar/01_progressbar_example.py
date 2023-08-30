import asyncio

import flet as ft

name = "ProgressBar Example"


def example():
    t = ft.Text(value="Click the button...")
    pb = ft.ProgressBar(width=400, value=0)

    async def button_clicked(e):
        t.value = "Doing something..."
        await t.update_async()
        b.disabled = True
        await b.update_async()
        for i in range(0, 101):
            pb.value = i * 0.01
            await asyncio.sleep(0.1)
            await pb.update_async()
        t.value = "Click the button..."
        await t.update_async()
        b.disabled = False
        await b.update_async()

    b = ft.FilledTonalButton("Start", on_click=button_clicked)

    return ft.Column(
        [
            ft.Text(
                "Linear progress indicator", style=ft.TextThemeStyle.HEADLINE_SMALL
            ),
            ft.Column([t, pb]),
            ft.Text(
                "Indeterminate progress bar", style=ft.TextThemeStyle.HEADLINE_SMALL
            ),
            ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee"),
            b,
        ],
        width=400,
        height=400,
    )
