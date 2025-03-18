import flet as ft


def main(page):
    dd = ft.Dropdown(
        options=[
            ft.dropdown.Option("a", "Item A"),
            ft.dropdown.Option("b", "Item B"),
            ft.dropdown.Option("c", "Item C"),
        ],
        text_size=20,
        content_padding=20,
        bgcolor=ft.Colors.BLUE_200,
        filled=True,
        focused_color=ft.Colors.GREEN,
        focused_bgcolor=ft.Colors.CYAN_200,
        border_radius=30,
        border_color=ft.Colors.GREEN_800,
        focused_border_color=ft.Colors.GREEN_ACCENT_400,
        focused_border_width=5,
        alignment=ft.alignment.center,
    )

    dd1 = ft.Dropdown(
        options=[
            ft.dropdown.Option("a", "Item A"),
            ft.dropdown.Option("b", "Item B"),
            ft.dropdown.Option("c", "Item C"),
        ],
        border_radius=30,
        filled=True,
        border_color=ft.Colors.TRANSPARENT,
        bgcolor=ft.Colors.BLACK12,
        focused_border_color=ft.Colors.BLUE_100,
        focused_border_width=20,
        alignment=ft.alignment.center_right,
    )

    dd1_5 = ft.Dropdown(
        options=[
            ft.dropdown.Option("a", "Item A"),
            ft.dropdown.Option("b", "Item B"),
            ft.dropdown.Option("c", "Item C"),
        ],
        border_color=ft.Colors.PINK_ACCENT,
        focused_border_color=ft.Colors.GREEN_ACCENT_400,
        focused_border_width=25,
        border_radius=30,
        width=150,
    )

    dd2 = ft.Dropdown(
        options=[
            ft.dropdown.Option("a", "Item A"),
            ft.dropdown.Option("b", "Item B"),
            ft.dropdown.Option("c", "Item C"),
        ],
        text_size=30,
        border_radius=20,
        filled=True,
        border_width=0,
        focused_border_color=ft.Colors.GREEN_100,
        focused_border_width=10,
        content_padding=20,
        width=200,
        # height=50,
    )

    dd3 = ft.Dropdown(
        options=[
            ft.dropdown.Option(
                "a",
                "Item A",
                style=ft.ButtonStyle(
                    color={
                        ft.ControlState.HOVERED: ft.Colors.WHITE,
                        ft.ControlState.FOCUSED: ft.Colors.BLUE,
                        ft.ControlState.DEFAULT: ft.Colors.BLACK,
                    },
                    shape=ft.BeveledRectangleBorder(15),
                ),
            ),
            ft.dropdown.Option(
                "b",
                "Item B",
                style=ft.ButtonStyle(
                    color={
                        ft.ControlState.HOVERED: ft.Colors.WHITE,
                        ft.ControlState.FOCUSED: ft.Colors.BLUE,
                        ft.ControlState.DEFAULT: ft.Colors.BLACK,
                    },
                    shape=ft.BeveledRectangleBorder(15),
                ),
            ),
            ft.dropdown.Option(
                "c",
                "Item C",
                style=ft.ButtonStyle(
                    color={
                        ft.ControlState.HOVERED: ft.Colors.WHITE,
                        ft.ControlState.FOCUSED: ft.Colors.BLUE,
                        ft.ControlState.DEFAULT: ft.Colors.BLACK,
                    },
                    shape=ft.BeveledRectangleBorder(15),
                ),
            ),
        ],
        text_size=30,
        border_radius=20,
        filled=True,
        border_width=0,
        focused_border_color=ft.Colors.GREEN_100,
        focused_border_width=10,
        content_padding=20,
        width=200,
    )

    page.add(dd, dd1, dd1_5, dd2, dd3)


ft.app(target=main)
