import flet as ft
from gallerydata import GalleryData
from popup_color_item import PopupColorItem

gallery = GalleryData()

def main(page: ft.Page):

    ft.page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }
    
    def get_route_list(route):
        route_list = [item for item in route.split("/") if item !=""]
        return route_list

    def route_change(e):
        route_list = get_route_list(page.route)
        if len(route_list) == 0:
            page.go("/layout")
        elif len(route_list) == 1:
            display_control_group(route_list[0])
        elif len(route_list) == 2:
            display_control_examples(route_list[0], route_list[1])
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

    def display_control_examples(control_group_name, control_id):
        control_group = find_control_group_object(control_group_name)
        rail.selected_index=gallery.destinations_list.index(control_group)
        grid_item = find_grid_object(control_group_name, control_id)
        grid.visible = False
        examples.visible = True
        listview.controls = []
        control_name.value = grid_item.name
        control_description.value = grid_item.description

        for example in grid_item.examples:
            listview.controls.append(ft.Column(controls = [
            ft.Container(content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls = [
                ft.Text(example.name, style=ft.TextThemeStyle.TITLE_MEDIUM, weight=ft.FontWeight.W_500), 
                ft.IconButton(icon=ft.icons.CODE, on_click=show_code, data=example)
                ]),
                bgcolor=ft.colors.SECONDARY_CONTAINER,
                padding=5,
                border_radius=5
                ),
            ft.Row(controls = [
                ft.Container(content=example.example()), 
                ]), 
                ]
            )
        )
                
        page.update()

    def display_control_group(control_group_name):
        control_group = find_control_group_object(control_group_name)
        rail.selected_index=gallery.destinations_list.index(control_group)
        grid.visible = True
        examples.visible = False
        grid.controls = []
        listview.controls = []
        for grid_item in control_group.grid_items:
            grid.controls.append(ft.Container(
                on_click=grid_item_clicked,
                data=grid_item, 
                bgcolor=ft.colors.SECONDARY_CONTAINER,
                border_radius=5,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        #ft.Image(src=grid_item.image_file_name, width=40), 
                        ft.Text(value=grid_item.name, style=ft.TextThemeStyle.TITLE_SMALL)]
                    )
                ))
        page.update()

    def control_group_selected(e):
        control_group_name = gallery.destinations_list[e.control.selected_index].name
        page.go(f"/{control_group_name}")
        display_control_group(control_group_name)
    
    def grid_item_clicked(e):
        route = f"{page.route}/{e.control.data.id}"
        page.go(route)
        route_list = get_route_list(route)
        display_control_examples(route_list[0], route_list[1])

    def show_code(e):
        dlg.open = True
        code_example_name.value = e.control.data.name
        code_text = ft.Text(value=e.control.data.source_code, selectable=True)
        
        dlg.content = ft.Column(controls=[code_text], scroll="always")
        dlg.data = e.control.data.source_code
        page.update() 
    
    def get_destinations():
        destinations = []
        for destination in gallery.destinations_list:
            destinations.append(ft.NavigationRailDestination(icon=destination.icon, selected_icon=destination.selected_icon, label=destination.label))
        return destinations
    
    def theme_changed(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            dark_light_text.value = "Dark theme"
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            dark_light_text.value = "Light theme"
        page.update()


    dark_light_text = ft.Text("Light theme")
    
    rail = ft.Column(
        controls=[
            ft.NavigationRail(
                extended=True,
                expand=True,
                selected_index=0,
                min_width=100,
                min_extended_width=200,
                group_alignment=-0.9,
                destinations=get_destinations(),
                on_change=control_group_selected
            ),
            ft.Column(
                controls=[
                    ft.Row(controls=[
                        ft.IconButton(icon=ft.icons.BRIGHTNESS_2_OUTLINED, tooltip="Toggle brightness", on_click=theme_changed),
                        dark_light_text]),
                    ft.Row(controls=[
                        ft.PopupMenuButton(
                            icon=ft.icons.COLOR_LENS_OUTLINED,
                            items=[
                                PopupColorItem(color="deeppurple", name="Deep purple"),
                                PopupColorItem(color="indigo", name="Indigo"),
                                PopupColorItem(color="blue", name="Blue (default)"),
                                PopupColorItem(color="teal", name="Teal"),
                                PopupColorItem(color="green", name="Green"),
                                PopupColorItem(color="yellow", name="Yellow"),
                                PopupColorItem(color="orange", name="Orange"),
                                PopupColorItem(color="deeporange", name="Deep orange"),
                                PopupColorItem(color="pink", name="Pink"),
                            ]),
                        ft.Text("Seed color")
                    ])   
                ])
        ]
    )
    grid = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    control_name = ft.Text(style=ft.TextThemeStyle.HEADLINE_MEDIUM)
    control_description = ft.Text(style=ft.TextThemeStyle.BODY_MEDIUM)
    listview = ft.ListView(expand=True, spacing=10, padding=20, auto_scroll=False)

    examples = ft.Column(visible=False, expand=True, controls=[
        control_name, control_description, listview
    ])

    page.appbar = ft.AppBar(
        leading=ft.Image(src=f"logo.svg"),
        leading_width=40,
        title=ft.Text("Flet Controls Gallery"),
        center_title=True,
        bgcolor=ft.colors.INVERSE_PRIMARY,
    )
    
    def copy_to_clipboard(e):
        source_code = dlg.data
        page.set_clipboard(source_code)
        page.show_snack_bar(ft.SnackBar(ft.Text(f"Example source code copied to clipboard"), open=True))
    
    def close_dlg(e):
        dlg.open = False
        page.update()
    
    code_example_name = ft.Text("Example")

    dlg = ft.AlertDialog(
        title=code_example_name,
        actions=[
            ft.FilledButton("Copy to clipboard", on_click=copy_to_clipboard),
            ft.TextButton("Close", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.dialog = dlg

    page.theme_mode = ft.ThemeMode.LIGHT


    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                grid,
                examples
            ],
            expand=True,
        )
    )

    page.on_route_change = route_change
    print(f"Initial route: {page.route}")
    page.go(page.route)

ft.app(target=main, assets_dir="images", view=ft.WEB_BROWSER)