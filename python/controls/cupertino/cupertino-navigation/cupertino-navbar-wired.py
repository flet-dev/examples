import flet as ft


def main(page: ft.Page):
    page.title = "CupertinoNavigationBar Example"

    def on_nav_change(e):
        # print(e.control.label)
        if e.control.selected_index == 0:
            body.content.value = "Explore!"
        elif e.control.selected_index == 1:
            body.content.value = "Find Your Way!"
        else:
            body.content.value = "Your Favorites!"
        page.update()

    body = ft.SafeArea(ft.Text("Explore!"))
    page.navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=ft.Colors.AMBER_100,
        inactive_color=ft.Colors.GREY,
        active_color=ft.Colors.BLACK,
        on_change=on_nav_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="Favorites",
            ),
        ],
    )
    page.add(body)


ft.run(main)
