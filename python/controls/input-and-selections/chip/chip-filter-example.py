import flet as ft


def main(page: ft.Page):
    def amenity_selected(e):
        page.update()

    title = ft.Row([ft.Icon(ft.Icons.HOTEL_CLASS), ft.Text("Amenities")])
    amenities = ["Washer / Dryer", "Ramp access", "Dogs OK", "Cats OK", "Smoke-free"]
    amenity_chips = []

    for amenity in amenities:
        amenity_chips.append(
            ft.Chip(
                label=ft.Text(amenity),
                bgcolor=ft.Colors.GREEN_200,
                disabled_color=ft.Colors.GREEN_100,
                autofocus=True,
                on_select=amenity_selected,
            )
        )

    page.add(title, ft.Row(amenity_chips))


ft.run(main)
