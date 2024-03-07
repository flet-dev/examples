import logging
from pathlib import Path

import flet as ft
import flet.version

from controls_grid import ControlsGrid
from examples_view import ExamplesView
from gallerydata import GalleryData
from left_navigation_menu import LeftNavigationMenu

gallery = GalleryData()

logging.basicConfig(level=logging.INFO)


async def main(page: ft.Page):
    page.title = "Flet controls gallery"

    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }

    def get_route_list(route):
        route_list = [item for item in route.split("/") if item != ""]
        return route_list

    async def route_change(e):
        route_list = get_route_list(page.route)
        if len(route_list) == 0:
            await page.go_async("/layout")
        elif len(route_list) == 1:
            await display_controls_grid(control_group_name=route_list[0])
        elif len(route_list) == 2:
            examples_view.control_group_name = route_list[0]
            examples_view.control_name = route_list[1]
            await display_control_examples()
        else:
            print("Invalid route")

    async def display_controls_grid(control_group_name):
        controls_grid.display(control_group_name)
        left_nav.rail.selected_index = gallery.destinations_list.index(
            controls_grid.control_group
        )
        examples_view.visible = False
        examples_view.examples.controls = []
        await page.update_async()

    async def display_control_examples():
        examples_view.display()
        left_nav.rail.selected_index = gallery.destinations_list.index(
            examples_view.control_group
        )
        controls_grid.visible = False

        await page.update_async()

    left_nav = LeftNavigationMenu(gallery=gallery)

    controls_grid = ControlsGrid(gallery=gallery)

    examples_view = ExamplesView(gallery=gallery)

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

    await page.add_async(
        ft.Row(
            [left_nav, ft.VerticalDivider(width=1), controls_grid, examples_view],
            expand=True,
        )
    )

    page.on_route_change = route_change
    print(f"Initial route: {page.route}")
    await page.go_async(page.route)


ft.app(main)
