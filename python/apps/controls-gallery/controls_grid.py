import flet as ft


class ControlsGrid(ft.GridView):
    def __init__(self, gallery):
        super().__init__()
        self.expand = 1
        self.runs_count = 5
        self.max_extent = 250
        self.child_aspect_ratio = 3.0
        self.spacing = 10
        self.run_spacing = 10
        self.gallery = gallery
        self.control_group = self.gallery.destinations_list[0]

    def find_control_group_object(self, control_group_name):
        for control_group in self.gallery.destinations_list:
            if control_group.name == control_group_name:
                self.control_group = control_group

    async def grid_item_clicked(self, e):
        route = f"{self.page.route}/{e.control.data.id}"
        await self.page.go_async(route)

    def display(self, control_group_name):
        self.find_control_group_object(control_group_name)
        # left_nav.rail.selected_index = gallery.destinations_list.index(control_group)
        self.visible = True
        # examples.visible = False
        self.controls = []
        # listview.controls = []
        for grid_item in self.control_group.grid_items:
            self.controls.append(
                ft.Container(
                    on_click=self.grid_item_clicked,
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
