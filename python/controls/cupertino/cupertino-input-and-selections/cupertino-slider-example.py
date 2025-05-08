import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    def handle_change_start(e):
        slider_status.value = "Sliding"
        page.update()

    def handle_change(e):
        slider_value.value = str(e.control.value)
        page.update()

    def handle_change_end(e):
        slider_status.value = "Finished sliding"
        page.update()

    page.add(
        slider_value := ft.Text("0.0"),
        ft.CupertinoSlider(
            divisions=5,
            max=100,
            active_color=ft.Colors.PURPLE,
            thumb_color=ft.Colors.PURPLE,
            on_change_start=handle_change_start,
            on_change_end=handle_change_end,
            on_change=handle_change,
        ),
        slider_status := ft.Text(),
    )


ft.run(main)
