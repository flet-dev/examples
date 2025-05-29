import flet as ft


def main(page):
    dd1 = ft.Dropdown(
        options=[
            ft.dropdown.Option("a", "Item A"),
            ft.dropdown.Option("b", "Item B"),
            ft.dropdown.Option("c", "Item C"),
        ],
        text_size=20,
        content_padding=10,
        color=ft.Colors.PURPLE_200,
        bgcolor=ft.Colors.BLUE_200,
        filled=True,
        border_radius=30,
        border_color=ft.Colors.GREEN_800,
        focused_border_color=ft.Colors.GREEN_ACCENT_400,
        focused_border_width=5,
    )

    dd2 = ft.Dropdown(
        options=[
            ft.dropdown.Option("a", "Item A"),
            ft.dropdown.Option("b", "Item B"),
            ft.dropdown.Option("c", "Item C"),
        ],
        border_radius=30,
        filled=True,
        fill_color=ft.Colors.RED_400,
        border_color=ft.Colors.TRANSPARENT,
        bgcolor=ft.Colors.RED_200,
        color=ft.Colors.CYAN_400,
        focused_border_color=ft.Colors.PINK_300,
        focused_border_width=20,
    )

    dd3 = ft.Dropdown(
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
        border_width=5,
    )

    dd4 = ft.Dropdown(
        options=[
            ft.dropdown.Option("a", "Item A"),
            ft.dropdown.Option("b", "Item B"),
            ft.dropdown.Option("c", "Item C"),
        ],
        text_size=30,
        color=ft.Colors.ORANGE_ACCENT,
        border_radius=20,
        filled=True,
        border_width=0,
        autofocus=True,
        focused_border_color=ft.Colors.GREEN_100,
        focused_border_width=10,
        width=200,
        height=50,
    )

    dd5 = ft.Dropdown(
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
                    shape=ft.BeveledRectangleBorder(radius=15),
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
                    shape=ft.BeveledRectangleBorder(radius=15),
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
                    shape=ft.BeveledRectangleBorder(radius=15),
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

    page.add(dd1, dd2, dd3, ft.Container(dd4, padding=ft.padding.only(bottom=20)), dd5)


ft.run(main)
