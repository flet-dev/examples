import flet as ft


def main(page: ft.Page):
    page.title = "Card Example"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(
        ft.Card(
            shadow_color=ft.Colors.ON_SURFACE_VARIANT,
            content=ft.Container(
                width=400,
                padding=10,
                content=ft.Column(
                    controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.ALBUM),
                            title=ft.Text("The Enchanted Nightingale"),
                            subtitle=ft.Text(
                                "Music by Julie Gable. Lyrics by Sidney Stein."
                            ),
                            bgcolor=ft.Colors.GREY_400,
                        ),
                        ft.Row(
                            controls=[
                                ft.TextButton("Buy tickets"),
                                ft.TextButton("Listen"),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
            ),
        )
    )


ft.run(main)
