import logging
from pathlib import Path

import flet as ft
import flet.version

from components.controls_grid import ControlsGrid
from components.examples_view import ExamplesView
from components.gallery_view import GalleryView
from components.left_navigation_menu import LeftNavigationMenu
from gallerydata import GalleryData

gallery = GalleryData()

logging.basicConfig(level=logging.INFO)


def main(page: ft.Page):
    page.title = "Flet controls gallery"

    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }

    def get_route_list(route):
        route_list = [item for item in route.split("/") if item != ""]
        return route_list

    def route_change(e):
        route_list = get_route_list(page.route)

        if len(route_list) == 0:
            page.go("/layout")
        else:
            gallery.selected_control_group = gallery.get_control_group(route_list[0])
            if len(route_list) == 1:
                display_controls_grid()
            elif len(route_list) == 2:
                display_control_examples(route_list[1])
            else:
                print("Invalid route")

    def display_controls_grid():
        gallery_view.controls_grid.display()
        gallery_view.examples_view.visible = False
        page.update()

    def display_control_examples(control_name):
        gallery_view.examples_view.display(
            gallery.get_control(gallery.selected_control_group.name, control_name)
        )
        gallery_view.controls_grid.visible = False
        page.update()

    gallery_view = GalleryView(gallery)

    page.appbar = ft.AppBar(
        leading=ft.Container(padding=5, content=ft.Image(src=f"logo.svg")),
        leading_width=40,
        title=ft.Text("Flet Controls Gallery"),
        center_title=True,
        bgcolor=ft.colors.INVERSE_PRIMARY,
        actions=[
            ft.Container(
                padding=10, content=ft.Text(f"Flet version: {flet.version.version}")
            )
        ],
    )

    page.theme_mode = ft.ThemeMode.LIGHT
    page.on_error = lambda e: print("Page error:", e.data)

    page.add(gallery_view)
    page.on_route_change = route_change
    print(f"Initial route: {page.route}")
    page.go(page.route)


ft.app(main)
