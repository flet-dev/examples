import flet as ft


def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO

    def slider_change_start(e: ft.Event[ft.RangeSlider]):
        print(f"on_change_start: {e.control.start_value}, {e.control.end_value}")

    def slider_is_changing(e: ft.Event[ft.RangeSlider]):
        print(f"on_change: {e.control.start_value}, {e.control.end_value}")

    def slider_change_end(e: ft.Event[ft.RangeSlider]):
        print(f"on_change_end: {e.control.start_value}, {e.control.end_value}")
        message.value = f"on_change_end: {e.control.start_value}, {e.control.end_value}"
        page.update()

    page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    value="Range slider with events",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Container(height=30),
                ft.RangeSlider(
                    divisions=50,
                    min=0,
                    max=50,
                    start_value=10,
                    end_value=20,
                    on_change_start=slider_change_start,
                    on_change=slider_is_changing,
                    on_change_end=slider_change_end,
                ),
                message := ft.Text(),
            ],
        )
    )


ft.run(main)
