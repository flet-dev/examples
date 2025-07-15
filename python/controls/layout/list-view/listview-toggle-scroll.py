import asyncio
import flet as ft


async def main(page: ft.Page):
    def change_auto_scroll(e):
        print("Change auto scroll triggered")
        lv.auto_scroll = not lv.auto_scroll
        page.update()

    lv = ft.ListView(
        spacing=10,
        padding=20,
        width=150,
        auto_scroll=True,
        controls=[
            ft.Text(f"Line {i}", color=ft.Colors.ON_SECONDARY) for i in range(0, 60)
        ],
    )

    page.add(
        ft.Row(
            controls=[
                ft.Container(
                    content=lv,
                    bgcolor=ft.Colors.GREY_500,
                ),
                ft.Switch(
                    thumb_icon=ft.Icons.LIST_OUTLINED,
                    value=True,
                    label="Auto-scroll",
                    label_position=ft.LabelPosition.RIGHT,
                    on_change=change_auto_scroll,
                ),
            ],
            expand=True,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
    )

    for i in range(len(lv.controls), 120):
        await asyncio.sleep(1)
        lv.controls.append(ft.Text(f"Line {i}", color=ft.Colors.ON_SECONDARY))
        page.update()


ft.run(main)
