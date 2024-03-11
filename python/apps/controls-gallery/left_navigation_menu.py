import flet as ft

from gallerydata import GalleryData

# from popup_color_item import PopupColorItem


class PopupColorItem(ft.PopupMenuItem):
    def __init__(self, color, name):
        super().__init__()
        self.content = ft.Row(
            controls=[
                ft.Icon(name=ft.icons.COLOR_LENS_OUTLINED, color=color),
                ft.Text(name),
            ],
        )
        self.on_click = self.seed_color_changed
        self.data = color

    async def seed_color_changed(self, e):
        self.page.theme = self.page.dark_theme = ft.theme.Theme(
            color_scheme_seed=self.data
        )
        await self.page.update_async()


class NavigationItem(ft.Container):
    def __init__(self, destination, item_clicked):
        super().__init__()
        self.ink = True
        self.padding = 10
        self.border_radius = 5
        self.destination = destination
        self.icon = destination.icon
        self.text = destination.label
        self.content = ft.Row([ft.Icon(self.icon), ft.Text(self.text)])
        self.on_click = item_clicked


class NavigationColumn(ft.Column):
    def __init__(self, gallery):
        super().__init__()
        self.expand = 4
        self.spacing = 0
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
        e.control.content.controls[0].name = (
            e.control.destination.selected_icon
        )  # change icon to selected_icon
        e.control.bgcolor = (
            ft.colors.SECONDARY_CONTAINER
        )  # change container bgcolor to "selected" color
        self.controls[self.selected_index].content.controls[0].name = self.controls[
            self.selected_index
        ].destination.icon  # change selected_icon to icon for previously selected item

        self.controls[self.selected_index].bgcolor = (
            None  # change container color to no color for previously selected item
        )
        self.selected_index = e.control.destination.index
        self.page.go(f"/{e.control.destination.name}")

    def update_selected_item(self):
        for item in self.controls:
            item.bgcolor = None
        self.controls[self.selected_index].bgcolor = ft.colors.SECONDARY_CONTAINER
        self.update()


class LeftNavigationMenu(ft.Column):
    def __init__(self, gallery):
        super().__init__()
        self.gallery = gallery

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

    async def theme_changed(self, e):
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.dark_light_text.value = "Dark theme"
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.dark_light_text.value = "Light theme"
        await self.page.update_async()
