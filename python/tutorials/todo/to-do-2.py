import flet
from flet import Checkbox, Column, FloatingActionButton, Page, Row, TextField, icons


def main(page: Page):
    def add_clicked(e):
        tasks.controls.append(Checkbox(label=new_task.value))
        new_task.value = ""
        view.update()

    new_task = TextField(hint_text="Whats needs to be done?", expand=True)
    tasks = Column()
    view = Column(
        width=600,
        controls=[
            Row(
                controls=[
                    new_task,
                    FloatingActionButton(icon=icons.ADD, on_click=add_clicked),
                ],
            ),
            tasks,
        ],
    )

    page.horizontal_alignment = "center"
    page.add(view)


flet.app(target=main)
