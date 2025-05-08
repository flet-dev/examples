import flet as ft


def main(page: ft.Page):
    def save_to_favorites_clicked(e):
        e.control.label.value = "Saved to favorites"
        e.control.leading = ft.Icon(ft.Icons.FAVORITE_OUTLINED)
        e.control.disabled = True
        page.update()

    def open_google_maps(e):
        page.launch_url("https://maps.google.com")
        page.update()

    save_to_favourites = ft.Chip(
        label=ft.Text("Save to favourites"),
        leading=ft.Icon(ft.Icons.FAVORITE_BORDER_OUTLINED),
        bgcolor=ft.Colors.GREEN_200,
        disabled_color=ft.Colors.GREEN_100,
        autofocus=True,
        on_click=save_to_favorites_clicked,
    )

    open_in_maps = ft.Chip(
        label=ft.Text("9 min walk"),
        leading=ft.Icon(ft.Icons.MAP_SHARP),
        bgcolor=ft.Colors.GREEN_200,
        on_click=open_google_maps,
    )

    page.add(ft.Row([save_to_favourites, open_in_maps]))


ft.run(main)
