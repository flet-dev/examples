import flet as ft

name = "MenuBar Example"


def example():
    menubar = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor=ft.colors.RED_100,
            mouse_cursor={
                ft.MaterialState.HOVERED: ft.MouseCursor.WAIT,
                ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
            },
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("File"),
                # on_open=handle_on_open,
                # on_close=handle_on_close,
                # on_hover=handle_on_hover,
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("About"),
                        leading=ft.Icon(ft.icons.INFO),
                        style=ft.ButtonStyle(
                            bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}
                        ),
                        # on_click=handle_menu_item_click
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Save"),
                        leading=ft.Icon(ft.icons.SAVE),
                        style=ft.ButtonStyle(
                            bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}
                        ),
                        # on_click=handle_menu_item_click
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Quit"),
                        leading=ft.Icon(ft.icons.CLOSE),
                        style=ft.ButtonStyle(
                            bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}
                        ),
                        # on_click=handle_menu_item_click
                    ),
                ],
            ),
            ft.SubmenuButton(
                content=ft.Text("View"),
                # on_open=handle_on_open,
                # on_close=handle_on_close,
                # on_hover=handle_on_hover,
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("Zoom"),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Magnify"),
                                leading=ft.Icon(ft.icons.ZOOM_IN),
                                close_on_click=False,
                                style=ft.ButtonStyle(
                                    bgcolor={
                                        ft.MaterialState.HOVERED: ft.colors.PURPLE_200
                                    }
                                ),
                                # on_click=handle_menu_item_click
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Minify"),
                                leading=ft.Icon(ft.icons.ZOOM_OUT),
                                close_on_click=False,
                                style=ft.ButtonStyle(
                                    bgcolor={
                                        ft.MaterialState.HOVERED: ft.colors.PURPLE_200
                                    }
                                ),
                                # on_click=handle_menu_item_click
                            ),
                        ],
                    )
                ],
            ),
        ],
    )
    return ft.Row([menubar])
