import asyncio

import flet as ft


async def main(page: ft.Page):
    pb = ft.ProgressBar(width=400)
    pbl = ft.Text("Doing something...")

    page.add(
        ft.Text(
            "Linear progress indicator", theme_style=ft.TextThemeStyle.HEADLINE_SMALL
        ),
        ft.Column([pbl, pb]),
        ft.Text(
            "Indeterminate progress bar", theme_style=ft.TextThemeStyle.HEADLINE_SMALL
        ),
        ft.ProgressBar(
            width=400,
            color=ft.Colors.AMBER,
        ),
    )

    for i in range(0, 101):

        pb.value = i * 0.01
        await asyncio.sleep(0.1)
        if i == 100:
            pbl.value = "Finished!"
        page.update()


ft.run(main)
