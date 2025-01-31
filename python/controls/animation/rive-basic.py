import flet as ft


def main(page):
    page.add(
        ft.Rive(
            "https://cdn.rive.app/animations/vehicles.riv",
            placeholder=ft.ProgressBar(),
            width=300,
            height=200,
        )
    )


ft.app(main)
