import flet as ft

name = "SegmentedButton example"


def example():
    bg_container = ft.Container(height=100, expand=True, bgcolor=ft.colors.AMBER)

    async def handle_color_click(e):
        color = e.control.content.value
        print(f"{color}.on_click")
        bg_container.bgcolor = color.lower()
        await bg_container.update_async()

    def handle_on_hover(e):
        print(f"{e.control.content.value}.on_hover")

    menubar = ft.MenuBar(
        expand=True,
        controls=[
            ft.SubmenuButton(
                content=ft.Text("BgColors"),
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("B"),
                        leading=ft.Icon(ft.icons.COLORIZE),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Blue"),
                                style=ft.ButtonStyle(
                                    bgcolor={ft.MaterialState.HOVERED: ft.colors.BLUE}
                                ),
                                on_click=handle_color_click,
                                on_hover=handle_on_hover,
                            )
                        ],
                    ),
                    ft.SubmenuButton(
                        content=ft.Text("G"),
                        leading=ft.Icon(ft.icons.COLORIZE),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Green"),
                                style=ft.ButtonStyle(
                                    bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN}
                                ),
                                on_click=handle_color_click,
                                on_hover=handle_on_hover,
                            )
                        ],
                    ),
                    ft.SubmenuButton(
                        content=ft.Text("R"),
                        leading=ft.Icon(ft.icons.COLORIZE),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Red"),
                                style=ft.ButtonStyle(
                                    bgcolor={ft.MaterialState.HOVERED: ft.colors.RED}
                                ),
                                on_click=handle_color_click,
                                on_hover=handle_on_hover,
                            )
                        ],
                    ),
                ],
            )
        ],
    )
    return ft.Column(
        [
            ft.Row([menubar]),
            ft.Row([bg_container]),
        ]
    )
