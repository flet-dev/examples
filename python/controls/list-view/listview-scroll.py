import asyncio
import flet as ft


async def main(page: ft.Page):
    page.title = "Auto-scrolling ListView"

    page.add(
        lv := ft.ListView(
            expand=1,
            spacing=10,
            padding=20,
            auto_scroll=True,
            controls=[ft.Text(f"Line {i}") for i in range(0, 60)],
        )
    )

    for i in range(len(lv.controls), 120):
        await asyncio.sleep(1)
        lv.controls.append(ft.Text(f"Line {i}"))
        page.update()


ft.run(main)
