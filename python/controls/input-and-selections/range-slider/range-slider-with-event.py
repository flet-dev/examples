import flet as ft


def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO

    def slider_change_start(e):
        print(f"on_change_start: {e.control.start_value}, {e.control.end_value}")

    def slider_is_changing(e):
        print(f"on_change: {e.control.start_value}, {e.control.end_value}")

    def slider_change_end(e):
        print(f"on_change_end: {e.control.start_value}, {e.control.end_value}")
        t.value = f"on_change_end: {e.control.start_value}, {e.control.end_value}"
        page.update()

    t = ft.Text("")

    range_slider = ft.RangeSlider(
        min=0,
        max=50,
        start_value=10,
        end_value=20,
        on_change_start=slider_change_start,
        on_change=slider_is_changing,
        on_change_end=slider_change_end,
    )

    page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    "Range slider with events",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Container(height=30),
                range_slider,
                t,
            ],
        )
    )


ft.app(main)
