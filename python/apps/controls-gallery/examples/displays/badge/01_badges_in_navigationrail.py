import flet as ft

name = "Badges in NavigationRail example"


def example():
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon_content=ft.Badge(content=ft.Icon(ft.icons.PHONE), text="10"),
                label="Calls",
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Badge(content=ft.Icon(ft.icons.MAIL), text="5"),
                label="Mail",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    return ft.Row(
        [
            rail,
            ft.VerticalDivider(width=1),
            ft.Column(
                [ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True
            ),
        ],
        width=400,
        height=400,
    )
