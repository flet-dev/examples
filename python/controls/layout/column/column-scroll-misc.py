import flet as ft


def main(page: ft.Page):
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            track_color={
                ft.ControlState.HOVERED: ft.Colors.AMBER,
                ft.ControlState.DEFAULT: ft.Colors.TRANSPARENT,
            },
            track_visibility=True,
            track_border_color=ft.Colors.BLUE,
            thumb_visibility=True,
            thumb_color={
                ft.ControlState.HOVERED: ft.Colors.RED,
                ft.ControlState.DEFAULT: ft.Colors.GREY_300,
            },
            thickness=30,
            radius=15,
            main_axis_margin=5,
            cross_axis_margin=10,
            # interactive=False,
        )
    )

    cl = ft.Column(
        spacing=10,
        height=200,
        width=float("inf"),
        scroll=ft.ScrollMode.ALWAYS,
    )
    for i in range(0, 100):
        cl.controls.append(ft.Text(f"Text line {i}", key=str(i)))

    def scroll_to_offset(e):
        cl.scroll_to(offset=500, duration=1000)

    def scroll_to_start(e):
        cl.scroll_to(offset=0, duration=1000)

    def scroll_to_end(e):
        cl.scroll_to(offset=-1, duration=2000, curve=ft.AnimationCurve.EASE_IN_OUT)

    def scroll_to_key(e):
        cl.scroll_to(key="20", duration=1000)

    def scroll_to_delta(e):
        cl.scroll_to(delta=100, duration=200)

    def scroll_to_minus_delta(e):
        cl.scroll_to(delta=-100, duration=200)

    page.add(
        ft.Container(cl, border=ft.border.all(1)),
        ft.ElevatedButton("Scroll to offset 500", on_click=scroll_to_offset),
        ft.Row(
            [
                ft.ElevatedButton("Scroll -100", on_click=scroll_to_minus_delta),
                ft.ElevatedButton("Scroll +100", on_click=scroll_to_delta),
            ]
        ),
        ft.ElevatedButton("Scroll to key '20'", on_click=scroll_to_key),
        ft.Row(
            [
                ft.ElevatedButton("Scroll to start", on_click=scroll_to_start),
                ft.ElevatedButton("Scroll to end", on_click=scroll_to_end),
            ]
        ),
    )


ft.app(main)
