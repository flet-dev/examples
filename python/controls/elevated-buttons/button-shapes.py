import flet as ft


def main(page: ft.Page):
    page.padding = 30
    page.spacing = 30
    page.add(
        ft.ElevatedButton(
            "Stadium",
            style=ft.ButtonStyle(
                shape=ft.StadiumBorder(),
            ),
        ),
        ft.ElevatedButton(
            "Rounded rectangle",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
        ),
        ft.ElevatedButton(
            "Continuous rectangle",
            style=ft.ButtonStyle(
                shape=ft.CountinuosRectangleBorder(radius=30),
            ),
        ),
        ft.ElevatedButton(
            "Beveled rectangle",
            style=ft.ButtonStyle(
                shape=ft.BeveledRectangleBorder(radius=10),
            ),
        ),
        ft.ElevatedButton(
            "Circle",
            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
        ),
    )


ft.app(main)
