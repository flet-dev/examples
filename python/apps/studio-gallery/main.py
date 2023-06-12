import flet as ft
import counter
import to_do
import calculator
import drawing_tool


class AppTile(ft.ListTile):
    def __init__(self, name, view):
        super().__init__()
        # self.height = 70
        # self.padding = 10
        self.view = view
        # self.border_radius = 5
        self.bgcolor = ft.colors.SURFACE_VARIANT
        self.title = ft.Text(name)
        self.on_click = self.app_button_clicked
        self.name = name

    def app_button_clicked(self, e):
        e.control.page.views.append(
            ft.View(
                controls=[
                    ft.AppBar(title=ft.Text(f"{e.control.name} app")),
                    e.control.view,
                ],
            )
        )
        e.control.page.update()


def main(page: ft.Page):
    counter_tile = AppTile("Counter", view=counter.example())
    to_do_tile = AppTile("To-Do", view=to_do.example())
    calc_tile = AppTile("Calculator", view=calculator.example())
    drawing_tool_tile = AppTile("Drawing Tool", view=drawing_tool.example())

    page.add(
        ft.ListView(controls=[counter_tile, to_do_tile, calc_tile, drawing_tool_tile])
    )

    def view_pop(view):
        page.views.pop()
        top_view = page.views[0]
        page.go(top_view.route)

    page.on_view_pop = view_pop

    page.update()


ft.app(target=main)
