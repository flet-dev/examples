import flet as ft
import counter, to_do, calculator, drawing_tool, buttons, entry_form, charts


class AppTile(ft.ListTile):
    def __init__(self, name, view):
        super().__init__()
        self.view = view
        self.bgcolor = ft.colors.SURFACE_VARIANT
        self.title = ft.Text(name)
        self.on_click = self.app_button_clicked
        self.name = name

    def app_button_clicked(self, e):
        e.control.page.views.append(
            ft.View(
                controls=[
                    ft.AppBar(title=ft.Text(f"{e.control.name}")),
                    e.control.view,
                ],
            )
        )
        e.control.page.update()


def main(page: ft.Page):
    page.add(
        ft.ListView(
            controls=[
                AppTile("Counter", view=counter.example()),
                AppTile("To-Do", view=to_do.example()),
                AppTile("Calculator", view=calculator.example()),
                AppTile("Drawing Tool", view=drawing_tool.example()),
                AppTile("Buttons", view=buttons.example()),
                AppTile("Entry form", view=entry_form.example()),
                AppTile("Charts", view=charts.example()),
            ]
        )
    )

    def view_pop(view):
        page.views.pop()
        top_view = page.views[0]
        page.go(top_view.route)

    page.on_view_pop = view_pop
    page.window_width = 390
    page.window_height = 844
    page.update()


ft.app(target=main)
