from time import sleep
import flet as ft


def main(page: ft.Page):
    pr = ft.ProgressRing(width=16, height=16, stroke_width=2)
    prl = ft.Text("Wait for the completion...")
    page.add(
        ft.Text("Circular progress indicator", style=ft.TextThemeStyle.HEADLINE_SMALL),
        ft.Row([pr, prl]),
        ft.Text(
            "Indeterminate cicrular progress", style=ft.TextThemeStyle.HEADLINE_SMALL
        ),
        ft.Column(
            [ft.ProgressRing(), ft.Text("I'm going to run for ages...")],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    for i in range(0, 101):
        pr.value = i * 0.01
        sleep(0.1)
        if i == 100:
            prl.value = "Finished!"
        page.update()


ft.app(main)
