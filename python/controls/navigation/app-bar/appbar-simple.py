import flet as ft


def main(page: ft.Page):
    page.title = "AppBar Example"

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    page.appbar = ft.runBar(
        leading=ft.Icon(ft.Icons.PALETTE),
        leading_width=40,
        title=ft.Text("AppBar Example"),
        center_title=False,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.Icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
    page.add(ft.Text("Body!"))


ft.run(target=main)
