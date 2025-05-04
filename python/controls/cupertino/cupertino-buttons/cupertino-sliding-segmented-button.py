import flet as ft


def main(page):
    page.title = "CupertinoSlidingSegmentedButton example"
    page.theme_mode = ft.ThemeMode.LIGHT

    def handle_change(e):
        print(f"selected_index: {e.data}")
        page.show_dialog(ft.SnackBar(ft.Text(f"segment {int(e.data) + 1} chosen")))

    page.add(
        ft.CupertinoSlidingSegmentedButton(
            selected_index=1,
            thumb_color=ft.Colors.BLUE_400,
            on_change=handle_change,
            controls=[
                ft.Text("One"),
                ft.Text("Two"),
                ft.Text("Three"),
            ],
        ),
    )


ft.app(main)
