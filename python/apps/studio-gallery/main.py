import flet as ft


class AppButton(ft.Container):
    def __init__(self, name):
        super().__init__()
        self.height = 70
        self.padding = 10
        self.border_radius = 5
        self.bgcolor = ft.colors.SURFACE_VARIANT
        self.content = ft.Row([ft.Text(name)])
        self.on_click = self.app_button_clicked
        self.data = name

    def app_button_clicked(self, e):
        e.control.page.views.append(
            ft.View(
                controls=[
                    ft.AppBar(title=ft.Text(f"{e.control.data} app")),
                    ft.Text(f"{e.control.data} app"),
                ]
            )
        )
        e.control.page.update()


def main(page: ft.Page):
    counter = AppButton("Counter")

    to_do = AppButton("To-Do")

    page.add(ft.Column(controls=[counter, to_do]))

    def view_pop(view):
        page.views.pop()
        top_view = page.views[0]
        page.go(top_view.route)

    page.on_view_pop = view_pop

    page.update()


ft.app(target=main)
