import logging
from pathlib import Path

import flet as ft
import flet.version
import flet_fastapi
from gallerydata import GalleryData
from left_navigation_menu import LeftNavigationMenu
from controls_grid import ControlsGrid

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
            await display_control_group(route_list[0])
        elif len(route_list) == 2:
            await display_control_examples(route_list[0], route_list[1])
        else:
            print("Invalid route")

    async def display_control_group(control_group_name):
        grid.display(control_group_name=control_group_name)
        # control_group = find_control_group_object(control_group_name)
        left_nav.rail.selected_index = gallery.destinations_list.index(
            grid.control_group
        )
        # grid.visible = True
        examples.visible = False
        # grid.controls = []
        listview.controls = []
        # for grid_item in control_group.grid_items:
        #     grid.controls.append(
        #         ft.Container(
        #             on_click=grid_item_clicked,
        #             data=grid_item,
        #             bgcolor=ft.colors.SECONDARY_CONTAINER,
        #             border_radius=5,
        #             padding=15,
        #             content=ft.Row(
        #                 alignment=ft.MainAxisAlignment.START,
        #                 vertical_alignment=ft.MainAxisAlignment.CENTER,
        #                 controls=[
        #                     ft.Icon(name=ft.icons.FOLDER_OPEN),
        #                     ft.Text(
        #                         value=grid_item.name,
        #                         weight=ft.FontWeight.W_500,
        #                         size=14,
        #                     ),
        #                 ],
        #             ),
        #         )
        #     )
        await page.update_async()

    def find_control_group_object(control_group_name):
        for control_group in gallery.destinations_list:
            if control_group.name == control_group_name:
                return control_group

    def find_grid_object(control_group_name, control_id):
        control_group = find_control_group_object(control_group_name)
        for grid_item in control_group.grid_items:
            if grid_item.id == control_id:
                return grid_item

    async def display_control_examples(control_group_name, control_id):
        control_group = find_control_group_object(control_group_name)
        left_nav.rail.selected_index = gallery.destinations_list.index(control_group)
        grid_item = find_grid_object(control_group_name, control_id)
        grid.visible = False
        examples.visible = True
        listview.controls = []
        control_name.value = grid_item.name
        control_description.value = grid_item.description

        for example in grid_item.examples:
            listview.controls.append(
                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Text(
                                        example.name,
                                        style=ft.TextThemeStyle.TITLE_MEDIUM,
                                        weight=ft.FontWeight.W_500,
                                    ),
                                    ft.IconButton(
                                        content=ft.Image(
                                            src="github-mark.svg",
                                            width=24,
                                            height=24,
                                            color=ft.colors.ON_SURFACE,
                                        ),
                                        url=f"https://github.com/flet-dev/examples/blob/main/python/apps/controls-gallery/{example.file_name}",
                                        url_target="_blank",
                                    ),
                                ],
                            ),
                            bgcolor=ft.colors.SECONDARY_CONTAINER,
                            padding=5,
                            border_radius=5,
                        ),
                        ft.Container(
                            content=example.example(),
                            clip_behavior=ft.ClipBehavior.NONE,
                        ),
                    ],
                )
            )

        await page.update_async()

    async def display_control_group_old(control_group_name):
        control_group = find_control_group_object(control_group_name)
        left_nav.rail.selected_index = gallery.destinations_list.index(control_group)
        grid.visible = True
        examples.visible = False
        grid.controls = []
        listview.controls = []
        for grid_item in control_group.grid_items:
            grid.controls.append(
                ft.Container(
                    on_click=grid_item_clicked,
                    data=grid_item,
                    bgcolor=ft.colors.SECONDARY_CONTAINER,
                    border_radius=5,
                    padding=15,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(name=ft.icons.FOLDER_OPEN),
                            ft.Text(
                                value=grid_item.name,
                                weight=ft.FontWeight.W_500,
                                size=14,
                            ),
                        ],
                    ),
                )
            )
        await page.update_async()

    async def grid_item_clicked(e):
        route = f"{page.route}/{e.control.data.id}"
        await page.go_async(route)

    left_nav = LeftNavigationMenu(gallery=gallery)

    grid = ControlsGrid(gallery=gallery)

    control_name = ft.Text(style=ft.TextThemeStyle.HEADLINE_MEDIUM)
    control_description = ft.Text(style=ft.TextThemeStyle.BODY_MEDIUM)
    listview = ft.Column(expand=True, spacing=10, scroll=ft.ScrollMode.AUTO)

    examples = ft.Column(
        visible=False,
        expand=True,
        controls=[control_name, control_description, listview],
    )

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
            [left_nav, ft.VerticalDivider(width=1), grid, examples],
            expand=True,
        )
    )

    page.on_route_change = route_change
    print(f"Initial route: {page.route}")
    await page.go_async(page.route)


app = flet_fastapi.app(
    main, assets_dir=str(Path(__file__).resolve().parent.joinpath("assets"))
)

if __name__ == "__main__":
    ft.app(main, assets_dir="assets")
