import flet as ft


def main(page: ft.Page):
    ts = ft.TextStyle(
        size=22,
        weight=ft.FontWeight.W_600,
        decoration=ft.TextDecoration(
            ft.TextDecoration.UNDERLINE | ft.TextDecoration.OVERLINE
        ),
        decoration_style=ft.TextDecorationStyle(ft.TextDecorationStyle.WAVY),
    )

    page.add(
        ft.SelectionArea(
            content=ft.Column(
                [
                    ft.Text("Selectable text", color=ft.Colors.GREEN, style=ts),
                    ft.Text("Also selectable", color=ft.Colors.GREEN, style=ts),
                ]
            )
        )
    )
    page.add(ft.Text("Not selectable", color=ft.Colors.RED, style=ts))


ft.app(main)
