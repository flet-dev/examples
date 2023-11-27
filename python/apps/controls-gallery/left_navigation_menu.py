import flet as ft
from popup_color_item import PopupColorItem
from gallerydata import GalleryData


class LeftNavigationMenu(ft.Column):
    def __init__(self, gallery):
        super().__init__()
        self.gallery = gallery
        self.rail = ft.NavigationRail(
            extended=True,
            expand=True,
            selected_index=0,
            min_width=100,
            min_extended_width=200,
            group_alignment=-0.9,
            destinations=self.get_destinations(),
            on_change=self.control_group_selected,
        )

        self.dark_light_text = ft.Text("Light theme")

        self.controls = [
            self.rail,
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.BRIGHTNESS_2_OUTLINED,
                                tooltip="Toggle brightness",
                                on_click=self.theme_changed,
                            ),
                            self.dark_light_text,
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
        ]

    def get_destinations(self):
        destinations = []
        for destination in self.gallery.destinations_list:
            destinations.append(
                ft.NavigationRailDestination(
                    icon=destination.icon,
                    selected_icon=destination.selected_icon,
                    label=destination.label,
                )
            )
        return destinations

    async def control_group_selected(self, e):
        control_group_name = self.gallery.destinations_list[
            e.control.selected_index
        ].name
        await self.page.go_async(f"/{control_group_name}")

    async def theme_changed(self, e):
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.dark_light_text.value = "Dark theme"
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.dark_light_text.value = "Light theme"
        await self.page.update_async()
