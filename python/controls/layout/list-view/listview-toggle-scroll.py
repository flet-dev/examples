from time import sleep
import flet as ft


def main(page: ft.Page):
    page.title = "Auto-scrolling ListView"

    def change_auto_scroll(e):
        print("Change auto scroll triggered")
        lv.auto_scroll = not lv.auto_scroll
        page.update()

    lv = ft.ListView(spacing=10, padding=20, width=150, auto_scroll=True)
    lvc = ft.Container(
        content=lv,
        bgcolor=ft.Colors.GREY_500,
    )
    sw = ft.Switch(
        thumb_icon=ft.Icons.LIST_OUTLINED,
        value=True,
        label="Auto-scroll",
        label_position=ft.LabelPosition.RIGHT,
        on_change=change_auto_scroll,
    )

    c = ft.Row(
        [lvc, sw],
        expand=True,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    count = 1

    for i in range(0, 60):
        lv.controls.append(ft.Text(f"Line {count}", color=ft.Colors.ON_SECONDARY))
        count += 1

    page.add(c)

    for i in range(0, 60):
        sleep(1)
        lv.controls.append(ft.Text(f"Line {count}", color=ft.Colors.ON_SECONDARY))
        count += 1
        page.update()


ft.app(main)
