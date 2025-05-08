import flet as ft
import flet_lottie as fl


def main(page: ft.Page):
    l = fl.Lottie(
        src="https://raw.githubusercontent.com/xvrh/lottie-flutter/refs/heads/master/example/assets/Logo/LogoSmall.json",
        reverse=False,
        animate=True,
    )
    c1 = ft.Container(content=l, bgcolor=ft.Colors.AMBER_ACCENT, padding=50)
    page.add(c1)


ft.run(main)
