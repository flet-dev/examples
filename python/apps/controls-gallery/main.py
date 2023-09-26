import logging
from pathlib import Path

import flet as ft
import flet.version
import flet_fastapi
from gallerydata import GalleryData
from popup_color_item import PopupColorItem

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
        rail.selected_index = gallery.destinations_list.index(control_group)
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

    async def display_control_group(control_group_name):
        control_group = find_control_group_object(control_group_name)
        rail.selected_index = gallery.destinations_list.index(control_group)
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

    async def control_group_selected(e):
        control_group_name = gallery.destinations_list[e.control.selected_index].name
        await page.go_async(f"/{control_group_name}")

    async def grid_item_clicked(e):
        route = f"{page.route}/{e.control.data.id}"
        await page.go_async(route)

    def get_destinations():
        destinations = []
        for destination in gallery.destinations_list:
            destinations.append(
                ft.NavigationRailDestination(
                    icon=destination.icon,
                    selected_icon=destination.selected_icon,
                    label=destination.label,
                )
            )
        return destinations

    async def theme_changed(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            dark_light_text.value = "Dark theme"
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            dark_light_text.value = "Light theme"
        await page.update_async()

    dark_light_text = ft.Text("Light theme")

    rail = ft.NavigationRail(
        extended=True,
        expand=True,
        selected_index=0,
        min_width=100,
        min_extended_width=200,
        group_alignment=-0.9,
        destinations=get_destinations(),
        on_change=control_group_selected,
    )

    left_nav = ft.Column(
        controls=[
            rail,
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.BRIGHTNESS_2_OUTLINED,
                                tooltip="Toggle brightness",
                                on_click=theme_changed,
                            ),
                            dark_light_text,
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.PopupMenuButton(
                                icon=ft.icons.COLOR_LENS_OUTLINED,
                                items=[
                                    PopupColorItem(
                                        color="deeppurple", name="Deep purple"
                                    ),
                                    PopupColorItem(color="indigo", name="Indigo"),
                                    PopupColorItem(color="blue", name="Blue (default)"),
                                    PopupColorItem(color="teal", name="Teal"),
                                    PopupColorItem(color="green", name="Green"),
                                    PopupColorItem(color="yellow", name="Yellow"),
                                    PopupColorItem(color="orange", name="Orange"),
                                    PopupColorItem(
                                        color="deeporange", name="Deep orange"
                                    ),
                                    PopupColorItem(color="pink", name="Pink"),
                                ],
                            ),
                            ft.Text("Seed color"),
                        ]
                    ),
                ]
            ),
        ],
    )
    grid = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=250,
        child_aspect_ratio=3.0,
        spacing=10,
        run_spacing=10,
    )

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
