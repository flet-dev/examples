import flet as ft


def main(page: ft.Page):
    page.title = "Floating Action Button"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0
    page.scroll = ft.ScrollMode.HIDDEN

    # keeps track of the number of tiles already added
    count = 1

    def fab_pressed(e):
        nonlocal count  # to modify the count variable found in the outer scope
        page.add(
            ft.ListTile(
                title=ft.Text(f"Tile {count}"),
                bgcolor=ft.Colors.TEAL_300,
                leading=ft.Icon(
                    ft.Icons.CIRCLE_OUTLINED, color=ft.Colors.DEEP_ORANGE_300
                ),
                on_click=lambda x: print(x.control.title.value + " was clicked!"),
            )
        )
        page.show_dialog(ft.SnackBar(ft.Text("Tile was added successfully!")))
        count += 1

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=fab_pressed, bgcolor=ft.Colors.LIME_300
    )
    page.add(
        ft.Container(
            ft.Row(
                [
                    ft.Text(
                        "Floating Action Button Example",
                        style=ft.TextStyle(size=20, weight=ft.FontWeight.W_500),
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor=ft.Colors.BLUE,
            padding=ft.Padding.all(20),
        ),
        ft.Text("Press the FAB to add a tile!"),
    )


ft.run(main)
