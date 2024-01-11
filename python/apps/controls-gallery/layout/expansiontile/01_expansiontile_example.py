import flet as ft

name = "ExpansionTile example"


def example():
    return ft.Column(
        controls=[
            ft.ExpansionTile(
                title=ft.Text("ExpansionTile 1"),
                subtitle=ft.Text("Trailing expansion arrow icon"),
                affinity=ft.TileAffinity.PLATFORM,
                maintain_state=True,
                collapsed_text_color=ft.colors.RED,
                text_color=ft.colors.RED,
                controls=[ft.ListTile(title=ft.Text("This is sub-tile number 1"))],
            ),
            ft.ExpansionTile(
                title=ft.Text("ExpansionTile 2"),
                subtitle=ft.Text("Custom expansion arrow icon"),
                trailing=ft.Icon(ft.icons.ARROW_DROP_DOWN),
                collapsed_text_color=ft.colors.GREEN,
                text_color=ft.colors.GREEN,
                controls=[ft.ListTile(title=ft.Text("This is sub-tile number 2"))],
            ),
            ft.ExpansionTile(
                title=ft.Text("ExpansionTile 3"),
                subtitle=ft.Text("Leading expansion arrow icon"),
                affinity=ft.TileAffinity.LEADING,
                initially_expanded=True,
                collapsed_text_color=ft.colors.BLUE,
                text_color=ft.colors.BLUE,
                controls=[
                    ft.ListTile(title=ft.Text("This is sub-tile number 3")),
                    ft.ListTile(title=ft.Text("This is sub-tile number 4")),
                    ft.ListTile(title=ft.Text("This is sub-tile number 5")),
                ],
            ),
        ]
    )
