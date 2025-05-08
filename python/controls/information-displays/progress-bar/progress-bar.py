from time import sleep

import flet as ft


def main(page: ft.Page):
    pb = ft.ProgressBar(width=400)
    pbl = ft.Text("Doing something...")

    page.add(
        ft.Text("Linear progress indicator", style=ft.TextThemeStyle.HEADLINE_SMALL),
        ft.Column([pbl, pb]),
        ft.Text("Indeterminate progress bar", style=ft.TextThemeStyle.HEADLINE_SMALL),
        ft.ProgressBar(width=400, color=ft.Colors.AMBER, bgcolor="#eeeeee"),
    )

    for i in range(0, 101):

        pb.value = i * 0.01
        sleep(0.1)
        if i == 100:
            pbl.value = "Finished!"
        page.update()


ft.run(main)
