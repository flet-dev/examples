import flet as ft

name = "Font with variable weight"


def example():
    class Example(ft.Column):
        def __init__(self):
            super().__init__()
            self.t = ft.Text(
                "This is rendered with Roboto Slab",
                size=30,
                font_family="RobotoSlab",
                weight=ft.FontWeight.W_100,
            )
            self.controls = [
                self.t,
                ft.Slider(
                    min=100,
                    max=900,
                    divisions=8,
                    label="{value}",
                    width=500,
                    on_change=self.width_changed,
                ),
            ]

        # happens when example is added to the page (when user chooses the Text control from the grid)
        def did_mount(self):
            self.page.fonts["RobotoSlab"] = "RobotoSlab[wght].ttf"
            self.page.update()

        async def width_changed(self, e):
            self.t.weight = f"w{int(e.control.value)}"
            await self.t.update_async()

    example = Example()

    return example
