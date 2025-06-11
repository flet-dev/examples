import itertools
#import logging
from dataclasses import dataclass, field

import flet as ft

#logging.basicConfig(level=logging.DEBUG)

task_id = itertools.count(1)


@dataclass
class TaskItem:
    name: str
    completed: bool = False
    edit_mode: bool = False
    new_name: str = ""
    id: int = field(default_factory=lambda: next(task_id))

    def toggle_task_status(self):
        self.completed = not self.completed

    def edit(self):
        self.new_name = self.name
        self.edit_mode = True

    def set_new_name(self, new_name: str):
        self.new_name = new_name

    def complete_edit(self):
        self.name = self.new_name
        self.edit_mode = False


@dataclass
class TodoState:
    tasks: list[TaskItem] = field(default_factory=list)
    tabs: list[str] = field(default_factory=lambda: ["all", "active", "completed"])
    selected_tab: str = "all"
    new_task_name: str = ""

    def get_tasks(self) -> list[TaskItem]:
        return list(
            filter(
                lambda task: self.selected_tab == "all"
                or self.selected_tab == "active"
                and not task.completed
                or self.selected_tab == "completed"
                and task.completed,
                self.tasks,
            )
        )

    def active_tasks_number(self):
        return len([task for task in self.tasks if not task.completed])

    def set_new_task_name(self, e: ft.ControlEvent):
        self.new_task_name = e.control.value

    def add_task(self):
        self.tasks.append(TaskItem(self.new_task_name))
        self.new_task_name = ""

    def tab_changed(self, e):
        self.selected_tab = self.tabs[e.control.selected_index]

    def delete_task(self, task: TaskItem):
        self.tasks.remove(task)

    def clear_completed(self):
        self.tasks = list(filter(lambda task: not task.completed, self.tasks))


def TaskView(state: TodoState, task: TaskItem):
    return (
        ft.Row(
            key=task.id,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Checkbox(
                    value=task.completed,
                    label=task.name,
                    on_change=lambda: task.toggle_task_status(),
                ),
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=lambda: task.edit(),
                        ),
                        ft.IconButton(
                            ft.Icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=lambda: state.delete_task(task),
                        ),
                    ],
                ),
            ],
        )
        if not task.edit_mode
        else ft.Row(
            key=task.id,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.TextField(
                    value=task.new_name,
                    on_change=lambda e: task.set_new_name(e.control.value),
                    expand=1,
                ),
                ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.Colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=lambda: task.complete_edit(),
                ),
            ],
        )
    )


def Header():
    return ft.Row(
        [
            ft.Text(
                value="Todos",
                theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM,
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )


def Footer(state: TodoState):
    return ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text(f"{state.active_tasks_number()} items left"),
            ft.OutlinedButton(
                content="Clear completed",
                on_click=state.clear_completed,
            ),
        ],
    )


def main(page: ft.Page):
    state = TodoState()

    page.add(
        ft.ControlBuilder(
            state,
            lambda state: ft.Column(
                [
                    Header(),
                    ft.Row(
                        controls=[
                            ft.TextField(
                                hint_text="What needs to be done?",
                                on_submit=state.add_task,
                                value=state.new_task_name,
                                on_change=state.set_new_task_name,
                                expand=True,
                            ),
                            ft.FloatingActionButton(
                                icon=ft.Icons.ADD, on_click=state.add_task
                            ),
                        ],
                    ),
                    ft.Column(
                        spacing=25,
                        controls=[
                            ft.Tabs(
                                scrollable=False,
                                selected_index=state.tabs.index(state.selected_tab),
                                on_change=state.tab_changed,
                                tabs=[ft.Tab(label=tab) for tab in state.tabs],
                            ),
                            ft.Column(
                                [TaskView(state, task) for task in state.get_tasks()]
                            ),
                            Footer(state),
                        ],
                    ),
                ]
            ),
        )
    )


ft.run(main)
