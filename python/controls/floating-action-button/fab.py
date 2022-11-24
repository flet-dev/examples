import flet as ft


def main(page: ft.Page):
    page.title = "Floating Action Button"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.auto_scroll = True
    page.scroll = ft.ScrollMode.HIDDEN
    page.appbar = ft.AppBar(
        title=ft.Text(
            "Floating Action Button", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK87
        ),
        bgcolor=ft.colors.BLUE,
        center_title=True,
        actions=[
            ft.IconButton(ft.icons.MENU, tooltip="Menu", icon_color=ft.colors.BLACK87)
        ],
        color=ft.colors.WHITE,
    )

    # keeps track of the number of tiles already added
    page.count = 0

    def fab_pressed(e):
        page.add(ft.ListTile(title=ft.Text(f"Tile {page.count}")))
        page.show_snack_bar(
            ft.SnackBar(ft.Text("Tile was added successfully!"), open=True)
        )
        page.count += 1

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click=fab_pressed, bgcolor=ft.colors.LIME_300
    )
    page.add(ft.Text("Press the FAB to add a tile!"))


ft.app(target=main)
