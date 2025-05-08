import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(
        ft.ExpansionTile(
            title=ft.Text("Expansion Tile with changing borders"),
            subtitle=ft.Text("Tile border changes when expanded"),
            bgcolor=ft.Colors.BLUE_GREY_200,
            collapsed_bgcolor=ft.Colors.BLUE_GREY_200,
            affinity=ft.TileAffinity.PLATFORM,
            maintain_state=True,
            shape=ft.StadiumBorder(),
            collapsed_shape=ft.StadiumBorder(),
            collapsed_text_color=ft.Colors.GREY_800,
            text_color=ft.Colors.GREY_800,
            controls=[
                ft.ListTile(
                    title=ft.Text("A sub-tile"),
                    bgcolor=ft.Colors.BLUE_GREY_200,
                    # shape=ft.StadiumBorder(),
                ),
                ft.ListTile(
                    title=ft.Text("Another sub-tile"),
                    bgcolor=ft.Colors.BLUE_GREY_200,
                    # shape=ft.StadiumBorder(),
                ),
            ],
        ),
    )


ft.run(main)
