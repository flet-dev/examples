import flet as ft


def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0

    bg_container = ft.Ref[ft.Container]()

    def handle_color_click(e):
        color = e.control.content.value
        print(f"{color}.on_click")
        bg_container.current.content.value = f"{color} background color"
        bg_container.current.bgcolor = color.lower()
        page.update()

    def handle_alignment_click(e):
        print("in handle alignment click method")
        print(
            f"bg_container.alignment: {bg_container.alignment}, bg_container.content: {bg_container.content}"
        )
        bg_container.current.alignment = e.control.data
        # page.update()
        # bg_container.alignment = e.control.data
        print(
            f"e.control.content.value: {e.control.content.value}, e.control.data: {e.control.data}"
        )
        page.update()

    def handle_on_hover(e):
        print(f"{e.control.content.value}.on_hover")

    bg_container = ft.Container(
        # ref=bg_container,
        expand=True,
        bgcolor=ft.Colors.SURFACE_TINT,
        alignment=ft.Alignment.CENTER,
        content=ft.Text(
            "Choose a bgcolor from the menu",
            style=ft.TextStyle(size=24, weight=ft.FontWeight.BOLD),
        ),
    )
    menubar = ft.MenuBar(
        expand=True,
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Change Body"),
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("BG Color"),
                        leading=ft.Icon(ft.Icons.COLORIZE),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Blue"),
                                style=ft.ButtonStyle(
                                    bgcolor={ft.ControlState.HOVERED: ft.Colors.BLUE}
                                ),
                                on_click=handle_color_click,
                                on_hover=handle_on_hover,
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Green"),
                                style=ft.ButtonStyle(
                                    bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN}
                                ),
                                on_click=handle_color_click,
                                on_hover=handle_on_hover,
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Red"),
                                style=ft.ButtonStyle(
                                    bgcolor={ft.ControlState.HOVERED: ft.Colors.RED}
                                ),
                                on_click=handle_color_click,
                                on_hover=handle_on_hover,
                            ),
                        ],
                    ),
                    ft.SubmenuButton(
                        content=ft.Text("Text alignment"),
                        leading=ft.Icon(ft.Icons.LOCATION_PIN),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("bottom_center"),
                                data=ft.Alignment.BOTTOM_CENTER,
                                style=ft.ButtonStyle(
                                    bgcolor={
                                        ft.ControlState.HOVERED: ft.Colors.GREY_100
                                    }
                                ),
                                on_click=handle_alignment_click,
                                # on_hover=handle_on_hover,
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("bottom_left"),
                                data=ft.Alignment.BOTTOM_LEFT,
                                style=ft.ButtonStyle(
                                    bgcolor={
                                        ft.ControlState.HOVERED: ft.Colors.GREY_100
                                    }
                                ),
                                on_click=handle_alignment_click,
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("top_center"),
                                data=ft.Alignment.TOP_CENTER,
                                style=ft.ButtonStyle(
                                    bgcolor={
                                        ft.ControlState.HOVERED: ft.Colors.GREY_100
                                    }
                                ),
                                on_click=handle_alignment_click,
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("center_left"),
                                data=ft.Alignment.CENTER_LEFT,
                                style=ft.ButtonStyle(
                                    bgcolor={
                                        ft.ControlState.HOVERED: ft.Colors.GREY_100
                                    }
                                ),
                                on_click=handle_alignment_click,
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("center_right"),
                                data=ft.Alignment.CENTER_RIGHT,
                                style=ft.ButtonStyle(
                                    bgcolor={
                                        ft.ControlState.HOVERED: ft.Colors.GREY_100
                                    }
                                ),
                                on_click=handle_alignment_click,
                            ),
                        ],
                    ),
                ],
            )
        ],
    )

    page.add(
        ft.Row([menubar]),
        ft.Container(
            ref=bg_container,
            expand=True,
            bgcolor=ft.Colors.SURFACE_TINT,
            content=ft.Text(
                "Choose a bgcolor from the menu",
                style=ft.TextStyle(size=24, weight=ft.FontWeight.BOLD),
            ),
            alignment=ft.Alignment.CENTER,
        ),
    )


ft.run(main)
