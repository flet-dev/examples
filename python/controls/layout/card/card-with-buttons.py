import flet as ft


def main(page: ft.Page):
    page.title = "Card Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.ALBUM),
                            title=ft.Text("The Enchanted Nightingale"),
                            subtitle=ft.Text(
                                "Music by Julie Gable. Lyrics by Sidney Stein."
                            ),
                            bgcolor=ft.Colors.GREY_400,
                        ),
                        ft.Row(
                            [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            ),
            shadow_color=ft.Colors.ON_SURFACE_VARIANT,
        )
    )


ft.run(main)
