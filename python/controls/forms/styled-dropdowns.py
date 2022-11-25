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
        color=ft.colors.PINK,
        bgcolor=ft.colors.BLUE_200,
        filled=True,
        focused_color=ft.colors.GREEN,
        focused_bgcolor=ft.colors.CYAN_200,
        border_radius=30,
        border_color=ft.colors.GREEN_800,
        focused_border_color=ft.colors.GREEN_ACCENT_400,
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
        border_color=ft.colors.TRANSPARENT,
        bgcolor=ft.colors.BLACK12,
        focused_bgcolor=ft.colors.BLUE_100,
        alignment=ft.alignment.center_right,
    )

    dd1_5 = ft.Dropdown(
        options=[
            ft.dropdown.Option("a", "Item A"),
            ft.dropdown.Option("b", "Item B"),
            ft.dropdown.Option("c", "Item C"),
        ],
        border_radius=30,
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
        focused_bgcolor=ft.colors.GREEN_100,
        content_padding=20,
        height=50,
    )

    page.add(dd, dd1, dd1_5, dd2)


ft.app(target=main)
