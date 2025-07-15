import flet as ft


def main(page: ft.Page):
    def handle_column_scroll(e: ft.OnScrollEvent[ft.Column]):
        print(
            f"Type: {e.event_type}, pixels: {e.pixels}, min_scroll_extent: {e.min_scroll_extent}, max_scroll_extent: {e.max_scroll_extent}"
        )

    page.add(
        ft.Container(
            border=ft.Border.all(1),
            content=ft.Column(
                spacing=10,
                height=200,
                width=200,
                scroll=ft.ScrollMode.ALWAYS,
                on_scroll=handle_column_scroll,
                controls=[
                    ft.Text(f"Text line {i}", scroll_key=str(i)) for i in range(0, 50)
                ],
            ),
        ),
    )


ft.run(main)
