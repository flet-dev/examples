import flet as ft


def main(page: ft.Page):

    appbar = ft.AppBar(leading=ft.TextButton("Edit"), title=ft.Text("Chats"), actions=[ft.IconButton(icon=ft.icons.NEW_LABEL)])
    bottom_navigation_bar = ft.NavigationBar(destinations=[
            ft.NavigationDestination(icon=ft.icons.CONTACT_EMERGENCY, label="Contacts",),
            ft.NavigationDestination(icon=ft.icons.CHAT, label="Chats",),
            ft.NavigationDestination(
                icon=ft.icons.SETTINGS,
                label="Settings",
            ),
        ])

    page.appbar = appbar
    page.navigation_bar = bottom_navigation_bar
    page.add(
        ft.Text("Fletogram")
    )


ft.app(target=main)