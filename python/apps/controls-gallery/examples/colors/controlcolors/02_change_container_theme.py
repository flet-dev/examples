import flet as ft

name = "Change container theme colors"


def example():
    async def change_primary_color(e):
        container.theme = ft.Theme(
            color_scheme=ft.ColorScheme(primary=primary_color.value)
        )
        primary_color.value = ""
        await container.update_async()
        await primary_color.update_async()

    container = ft.Container(
        width=200,
        height=200,
        border=ft.border.all(1, ft.colors.BLACK),
        content=ft.FilledButton("Primary color"),
    )

    primary_color = ft.TextField(label="Primary color value", width=500)
    return ft.Column(
        controls=[
            container,
            ft.Row(
                controls=[
                    primary_color,
                    ft.FilledButton(
                        text="Change Primary color in Container",
                        on_click=change_primary_color,
                    ),
                ]
            ),
        ]
    )
