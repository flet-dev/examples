import flet as ft

name = "Color palettes"


def example():
    class ColorSwatch():
        def __init__(self, name, display_name, accent=True):
            self.name = name
            self.display_name = display_name
            self.accent = accent

    class Color():
        def __init__(self, swatch, shade="", accent=False):
            if not accent:
                self.name = f"{swatch.name}{shade}"
                self.display_name = f"{swatch.display_name}_{shade}"
            else:
                self.name = f"{swatch.name}accent{shade}"
                self.display_name = f"{swatch.display_name}_ACCENT_{shade}"

            
    SHADES = ['50', '100', '200', '300', '400', '500', '600', '700', '800', '900']
    ACCENT_SHADES = ['100', '200', '400', '700']

    swatches = [
        ColorSwatch(name="red", display_name="RED"),
        ColorSwatch(name="pink", display_name="PINK"),
        ColorSwatch(name="purple", display_name="PURPLE"),
        ColorSwatch(name="grey", display_name="GREY", accent=False)
        ]
    
    def generate_color_names(swatch):
        colors = []
        base_color = Color(swatch=swatch)
        colors.append(base_color)
        for shade in SHADES:
            color = Color(swatch=swatch, shade=shade)
            colors.append(color)
        if swatch.accent:
            for shade in ACCENT_SHADES:
                color = Color(swatch=swatch, shade=shade, accent=True)
                colors.append(color)
        return colors


    grid = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=500,
        child_aspect_ratio=0.5,
        spacing=10,
        run_spacing=10,
    )
    
    grid.controls = []
    
    for swatch in swatches:
        swatch_colors = ft.Column(spacing=0, controls=[])
        grid.controls.append(ft.Column([ft.Container(border_radius=10, content=swatch_colors)]))
        for color in generate_color_names(swatch):
            swatch_colors.controls.append(ft.Container(
                height=50,
                alignment=ft.alignment.center,
                bgcolor=color.name,
                content=ft.Text(color.display_name, weight=ft.FontWeight.W_500)))

    # for color in ft.colors:
    #         grid.controls.append(
    #             ft.Container(
    #                 #on_click=grid_item_clicked,
    #                 #data=grid_item,
    #                 bgcolor=color,
    #                 border_radius=5,
    #                 padding=15,
    #                 content=ft.Row(
    #                     alignment=ft.MainAxisAlignment.START,
    #                     vertical_alignment=ft.MainAxisAlignment.CENTER,
    #                     controls=[
    #                         ft.Icon(name=ft.icons.FOLDER_OPEN),
    #                         ft.Text(
    #                             value=color,
    #                             weight=ft.FontWeight.W_500,
    #                             size=14
    #                             )
                    
    #                     ]
    #                 )
    #             )
    #         )

    return grid