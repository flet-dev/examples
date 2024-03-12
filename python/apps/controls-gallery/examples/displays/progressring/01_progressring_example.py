import asyncio

import flet as ft

name = "ProgressRing Example"


def example():
    t = ft.Text(value="Click the button...")
    pr = ft.ProgressRing(width=16, height=16, stroke_width=2)

    async def button_clicked(e):
        t.value = "Doing something..."
        await t.update_async()
        b.disabled = True
        await b.update_async()
        for i in range(0, 101):
            pr.value = i * 0.01
            await asyncio.sleep(0.1)
            await pr.update_async()
        t.value = "Click the button..."
        await t.update_async()
        b.disabled = False
        await b.update_async()

    b = ft.FilledTonalButton("Start", on_click=button_clicked)

    return ft.Column(
        [
            ft.Text(
                "Circular progress indicator", style=ft.TextThemeStyle.HEADLINE_SMALL
            ),
            ft.Row([pr, t]),
            ft.Text(
                "Indeterminate cicrular progress",
                style=ft.TextThemeStyle.HEADLINE_SMALL,
            ),
            ft.Column(
                [ft.ProgressRing(), ft.Text("I'm going to run for ages...")],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            b,
        ],
        width=400,
        height=400,
    )
