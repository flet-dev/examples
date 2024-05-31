import flet as ft


class TodoApp(ft.UserControl):
    def build(self):
        self.new_task = ft.TextField(hint_text="What needs to be done?", expand=True)
        self.tasks_view = ft.Column()

        # application's root control (i.e. "view") containing all other controls
        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD, on_click=self.add_clicked
                        ),
                    ],
                ),
                self.tasks_view,
            ],
        )

    def add_clicked(self, e):
        self.tasks_view.controls.append(ft.Checkbox(label=self.new_task.value))
        self.new_task.value = ""
        self.update()


def main(page: ft.Page):
    page.title = "To-Do App"
    page.horizontal_alignment = "center"
    page.update()

    # create application instance
    todo = TodoApp()

    # add application's root control to the page
    page.add(todo)


ft.app(target=main)
