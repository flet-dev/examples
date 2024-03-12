import flet as ft

name = "Customize Theme colors"


def example():
    async def set_primary_color(e):
        e.control.page.theme = ft.Theme(
            color_scheme=ft.ColorScheme(
                primary=ft.colors.GREEN,
            ),
        )
        await e.control.page.update_async()

    return ft.FilledButton("Set Primary Color to GREEN", on_click=set_primary_color)
