import flet as ft


def main(page: ft.Page):
    l = ft.Lottie(
        src="https://raw.githubusercontent.com/xvrh/lottie-flutter/refs/heads/master/example/assets/Logo/LogoSmall.json",
        reverse=False,
        animate=True,
    )
    c1 = ft.Container(content=l, bgcolor=ft.Colors.AMBER_ACCENT, padding=50)
    page.add(c1)


ft.app(main)
