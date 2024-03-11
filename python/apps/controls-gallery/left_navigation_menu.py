import flet as ft

from gallerydata import GalleryData
from popup_color_item import PopupColorItem


class NavigationItem(ft.TextButton):
    def __init__(self, destination, item_clicked):
        super().__init__()
        self.destination = destination
        self.icon = destination.icon
        self.text = destination.label
        self.on_click = item_clicked


class NavigationColumn(ft.Column):
    def __init__(self, gallery):
        super().__init__()
        self.expand = 4
        self.scroll = ft.ScrollMode.ALWAYS
        self.width = 200
        self.gallery = gallery
        self.selected_index = 0
        self.controls = self.get_navigation_items()

    def get_navigation_items(self):
        navigation_items = []
        for destination in self.gallery.destinations_list:
            navigation_items.append(
                NavigationItem(destination, item_clicked=self.item_clicked)
            )
        return navigation_items

    def item_clicked(self, e):
        e.control.icon = (
            e.control.destination.selected_icon
        )  # change icon to selected_icon
        self.controls[self.selected_index].icon = self.controls[
            self.selected_index
        ].destination.icon  # change selected_icon to icon for previously selected item
        self.selected_index = e.control.destination.index
        self.page.go(f"/{e.control.destination.name}")


class LeftNavigationMenu(ft.Column):
    def __init__(self, gallery):
        super().__init__()
        self.gallery = gallery
        # self.expand = True
        # self.rail = ft.NavigationRail(
        #     extended=True,
        #     expand=True,
        #     selected_index=0,
        #     min_width=100,
        #     min_extended_width=200,
        #     group_alignment=-0.9,
        #     destinations=self.get_destinations(),
        #     on_change=self.control_group_selected,
        # )
        # self.rail = ft.Column(
        #     controls=self.get_navigation_items(),
        # )
        self.rail = NavigationColumn(gallery=gallery)

        self.dark_light_text = ft.Text("Light theme")

        self.controls = [
            self.rail,
            ft.Column(
                expand=1,
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
                ],
            ),
        ]

    # def get_destinations(self):
    #     destinations = []
    #     for destination in self.gallery.destinations_list:
    #         destinations.append(
    #             ft.NavigationRailDestination(
    #                 icon=destination.icon,
    #                 selected_icon=destination.selected_icon,
    #                 label=destination.label,
    #             )
    #         )
    #     return destinations

    # def get_navigation_items(self):
    #     navigation_items = []
    #     for destination in self.gallery.destinations_list:
    #         navigation_items.append(NavigationItem(destination))
    #     return navigation_items

    # async def control_group_selected(self, e):
    #     control_group_name = self.gallery.destinations_list[
    #         e.control.selected_index
    #     ].name
    #     await self.page.go_async(f"/{control_group_name}")

    # async def navigation_item_selected(self, e):
    #     control_group_name = "buttons"
    #     await self.page.go_async(f"/{control_group_name}")

    async def theme_changed(self, e):
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.dark_light_text.value = "Dark theme"
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.dark_light_text.value = "Light theme"
        await self.page.update_async()
