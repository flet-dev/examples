import flet as ft
import flet_rive as ftr


def main(page):
    page.add(
        ftr.Rive(
            "https://cdn.rive.app/animations/vehicles.riv",
            placeholder=ft.ProgressBar(),
            width=300,
            height=200,
        )
    )


ft.run(main)
