import flet as ft
import counter

examples = {"counter": counter.example}


class Example:
    def __init__(self, name, control):
        self.name = name
        self.control = control


# examples = [Example("Counter", counter.example())]


class AppButton(ft.Container):
    def __init__(self, name):
        super().__init__()
        self.height = 70
        self.padding = 10
        # self.ref_to_control = ref_to_control
        self.border_radius = 5
        self.bgcolor = ft.colors.SURFACE_VARIANT
        self.content = ft.Row([ft.Text(name)])
        self.on_click = self.app_button_clicked
        self.data = name

    def app_button_clicked(self, e):
        if e.control.data == "Counter":
            e.control.page.views.append(
                ft.View(
                    controls=[
                        ft.AppBar(title=ft.Text("Counter app")),
                        examples["counter"](),
                    ]
                )
                # ft.View("/", [ft.Text("Counter text")])
            )
            print(len(e.control.page.views))
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
