import flet as ft


def main(page):
    page.title = "CupertinoSlidingSegmentedButton example"
    page.theme_mode = ft.ThemeMode.LIGHT

    def handle_change(e):
        print(f"selected_index: {e.data}")
        page.add(ft.Text(f"segment {int(e.data) + 1} chosen"))
        page.update()

    page.add(
        ft.CupertinoSlidingSegmentedButton(
            selected_index=1,
            thumb_color=ft.Colors.BLUE_400,
            on_change=handle_change,
            padding=ft.padding.symmetric(0, 10),
            controls=[
                ft.Text("One"),
                ft.Text("Two"),
                ft.Text("Three"),
            ],
        ),
    )


ft.app(main)
