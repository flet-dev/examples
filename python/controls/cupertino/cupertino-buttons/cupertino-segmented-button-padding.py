import flet as ft


def main(page):
    page.theme_mode = ft.ThemeMode.LIGHT

    def handle_vertical_change(e):
        csb.controls[1].padding = ft.padding.only(
            top=e.control.value, bottom=e.control.value
        )
        page.update()

    def handle_horizontal_change(e):
        csb.controls[2].padding = ft.padding.only(
            left=e.control.value, right=e.control.value
        )
        page.update()

    csb = ft.CupertinoSegmentedButton(
        selected_index=1,
        selected_color=ft.Colors.RED_400,
        unselected_color=ft.Colors.GREY_400,
        on_change=lambda e: print(f"selected_index: {e.data}"),
        controls=[
            ft.Text("All"),
            ft.Container(
                padding=ft.padding.symmetric(30, 0),
                content=ft.Text("None"),
            ),
            ft.Container(
                padding=ft.padding.symmetric(0, 30),
                content=ft.Text("Some"),
            ),
        ],
    )

    vs = ft.Slider(
        label="{value}",
        min=0,
        max=50,
        divisions=50,
        value=30,
        on_change=handle_vertical_change,
    )
    hs = ft.Slider(
        label="{value}",
        min=0,
        max=50,
        divisions=50,
        value=30,
        on_change=handle_horizontal_change,
    )
    page.add(
        csb,
        ft.Text("Vertical padding button 1: "),
        vs,
        ft.Text("Horizontal padding button 2:"),
        hs,
        ft.Text(
            "*note that padding changes to one segment can effect padding on other segments*",
            style=ft.TextThemeStyle.LABEL_MEDIUM,
            color=ft.Colors.ORANGE_ACCENT,
        ),
    )


ft.app(main)
