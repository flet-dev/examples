import asyncio
import flet as ft


async def main(page: ft.Page):
    page.add(
        ft.Text(
            value="Circular progress indicator",
            theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
        ),
        ft.Row(
            controls=[
                ring1 := ft.ProgressRing(width=16, height=16, stroke_width=2),
                message1 := ft.Text("Wait for the completion..."),
            ]
        ),
        ft.Text(
            value="Indeterminate cicrular progress",
            theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
        ),
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[ft.ProgressRing(), ft.Text("I'm going to run for ages...")],
        ),
    )

    for i in range(0, 101):
        ring1.value = i * 0.01
        await asyncio.sleep(0.1)
        if i == 100:
            message1.value = "Finished!"
        page.update()


ft.run(main)
