import flet as ft


def main(page: ft.Page):
    def on_column_scroll(e: ft.OnScrollEvent):
        print(
            f"Type: {e.event_type}, pixels: {e.pixels}, min_scroll_extent: {e.min_scroll_extent}, max_scroll_extent: {e.max_scroll_extent}"
        )

    cl = ft.Column(
        spacing=10,
        height=200,
        width=200,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll=on_column_scroll,
    )
    for i in range(0, 50):
        cl.controls.append(ft.Text(f"Text line {i}", key=str(i)))

    page.add(
        ft.Container(cl, border=ft.border.all(1)),
    )


ft.app(main)
