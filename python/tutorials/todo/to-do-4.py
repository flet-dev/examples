import flet
from flet import (
    Checkbox,
    Column,
    FloatingActionButton,
    IconButton,
    Page,
    Row,
    TextField,
    colors,
    icons,
)


class Task:
    def __init__(self, app, name):
        self.app = app
        self.display_task = Checkbox(value=False, label=name)
        self.edit_name = TextField(expand=1)

        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_task,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        IconButton(
                            icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.edit_name,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        self.view = Column(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.view.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.view.update()

    def delete_clicked(self, e):
        self.app.delete_task(self)


class TodoApp:
    def __init__(self):
        self.tasks = []
        self.new_task = TextField(hint_text="Whats needs to be done?", expand=True)
        self.tasks_view = Column()

        # application's root control (i.e. "view") containing all other controls
        self.view = Column(
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
        task = Task(self, self.new_task.value)
        self.tasks.append(task)
        self.tasks_view.controls.append(task.view)
        self.new_task.value = ""
        self.view.update()

    def delete_task(self, task):
        self.tasks.remove(task)
        self.tasks_view.controls.remove(task.view)
        self.view.update()


def main(page: Page):
    page.title = "ToDo App"
    page.horizontal_alignment = "center"
    page.update()

    # create application instance
    app = TodoApp()

    # add application's root control to the page
    page.add(app.view)


flet.app(target=main)
