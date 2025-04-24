import flet as ft


def main(page: ft.Page):
    page.title = "Containers with different borders"

    c1 = ft.Container(
        bgcolor=ft.colors.AMBER,
        padding=15,
        border=ft.border.all(10, ft.Colors.PINK_600),
        border_radius=ft.border_radius.all(30),
        width=150,
        height=150,
    )

    c2 = ft.Container(
        bgcolor=ft.colors.DEEP_PURPLE,
        padding=15,
        border=ft.border.all(3, ft.Colors.LIGHT_GREEN_ACCENT),
        border_radius=ft.border_radius.only(top_left=10, bottom_right=10),
        width=150,
        height=150,
    )

    c3 = ft.Container(
        bgcolor=ft.colors.BLUE_GREY_900,
        padding=15,
        border=ft.border.symmetric(vertical=ft.BorderSide(8, ft.Colors.YELLOW_800)),
        width=150,
        height=150,
    )

    r = ft.Row([c1, c2, c3])
    page.add(r)


ft.app(main)
