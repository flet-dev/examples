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
            if shade=="":
                self.name = swatch.name
                self.display_name = swatch.display_name
            else:
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
        ColorSwatch(name="deeppurple", display_name="DEEP_PURPLE"),
        ColorSwatch(name="indigo", display_name="INDIGO"),
        ColorSwatch(name="blue", display_name="BLUE"),
        ColorSwatch(name="lightblue", display_name="LIGHT_BLUE"),
        ColorSwatch(name="cyan", display_name="CYAN"),
        ColorSwatch(name="teal", display_name="TEAL"),
        ColorSwatch(name="green", display_name="GREEN"),
        ColorSwatch(name="lightgreen", display_name="LIGHT_GREEN"),
        ColorSwatch(name="lime", display_name="LIME"),
        ColorSwatch(name="yellow", display_name="YELLOW"),
        ColorSwatch(name="amber", display_name="AMBER"),
        ColorSwatch(name="orange", display_name="ORANGE"),
        ColorSwatch(name="deeporange", display_name="DEEP_ORANGE"),
        ColorSwatch(name="brown", display_name="BROWN", accent=False),
        ColorSwatch(name="grey", display_name="GREY", accent=False),
        ColorSwatch(name="bluegrey", display_name="BLUE_GREY", accent=False)
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


    responsive_row = ft.ResponsiveRow(
        run_spacing=10,
        vertical_alignment=ft.CrossAxisAlignment.START
    )
    
    responsive_row.controls = []
    
    for swatch in swatches:
        swatch_colors = ft.Column(spacing=0, controls=[])
        responsive_row.controls.append(ft.Column(
            [ft.Container(border_radius=10, content=swatch_colors)],
            col={"sm": 6, "md": 4, "xl": 2}))
        for color in generate_color_names(swatch):
            swatch_colors.controls.append(ft.Container(
                height=50,
                alignment=ft.alignment.center,
                bgcolor=color.name,
                content=ft.Text(color.display_name, weight=ft.FontWeight.W_500)))


    return responsive_row