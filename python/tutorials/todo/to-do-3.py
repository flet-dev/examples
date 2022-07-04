import flet
from flet import (
    Checkbox,
    Column,
    FloatingActionButton,
    Page,
    Row,
    TextField,
    UserControl,
    icons,
)


class TodoApp(UserControl):
    def build(self):
        self.new_task = TextField(hint_text="Whats needs to be done?", expand=True)
        self.tasks_view = Column()

        # application's root control (i.e. "view") containing all other controls
        return Column(
            width=600,
            controls=[
                Row(
                    controls=[
                        self.new_task,
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.tasks_view,
            ],
        )

    def add_clicked(self, e):
        self.tasks_view.controls.append(Checkbox(label=self.new_task.value))
        self.new_task.value = ""
        self.update()


def main(page: Page):
    page.title = "ToDo App"
    page.horizontal_alignment = "center"
    page.update()

    # create application instance
    todo = TodoApp()

    # add application's root control to the page
    page.add(todo)


flet.app(target=main)
