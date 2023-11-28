import flet as ft


class ExamplesView(ft.Column):
    def __init__(self, gallery):
        super().__init__()
        self.gallery = gallery
        self.visible = False
        self.expand = True
        self.control_name_text = ft.Text(style=ft.TextThemeStyle.HEADLINE_MEDIUM)
        self.control_description = ft.Text(style=ft.TextThemeStyle.BODY_MEDIUM)
        self.examples = ft.Column(expand=True, spacing=10, scroll=ft.ScrollMode.AUTO)
        self.controls = [
            self.control_name_text,
            self.control_description,
            self.examples,
        ]
        self.control_group_name = None
        self.control_name = None

    def find_control_group_object(self):
        for control_group in self.gallery.destinations_list:
            if control_group.name == self.control_group_name:
                return control_group

    def find_grid_object(self):
        self.control_group = self.find_control_group_object()
        for grid_item in self.control_group.grid_items:
            if grid_item.id == self.control_name:
                print(grid_item.name, grid_item.parent.name)
                return grid_item

    def display(self):
        grid_item = self.find_grid_object()
        self.visible = True
        self.examples.controls = []
        self.control_name_text.value = grid_item.name
        self.control_description.value = grid_item.description

        for example in grid_item.examples:
            self.examples.controls.append(
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
