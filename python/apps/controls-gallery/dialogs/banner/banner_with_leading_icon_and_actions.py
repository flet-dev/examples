import flet as ft

name = "Banner with leading icon and actions"

def example():


    def close_banner(e):
        e.control.page.banner.open = False
        e.control.page.update()

    banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text(
            "Oops, there were some errors while trying to delete the file. What would you like me to do?"
        ),
        actions=[
            ft.TextButton("Retry", on_click=close_banner),
            ft.TextButton("Ignore", on_click=close_banner),
            ft.TextButton("Cancel", on_click=close_banner),
        ],
    )

    def show_banner_click(e):
        e.control.page.banner = banner
        e.control.page.banner.open = True
        e.control.page.update()
    
    return ft.ElevatedButton("Show Banner", on_click=show_banner_click)