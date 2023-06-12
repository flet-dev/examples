import flet as ft


def example():
    new_task = ft.TextField(
        hint_text="What needs to be done?",
        # on_submit=self.add_clicked,
        expand=True,
    )

    filter = ft.Tabs(
        selected_index=0,
        scrollable=False,
        # on_change=self.tabs_changed,
        tabs=[
            ft.Tab(text="all"),
            ft.Tab(text="active"),
            ft.Tab(text="completed"),
        ],
    )
    tasks = ft.Column(
        scroll=ft.ScrollMode.AUTO,
        expand=True,
        controls=[
            ft.Text("Task 1"),
            ft.Text("Task 2"),
            ft.Text("Task 3"),
            ft.Text("Task 4"),
            ft.Text("Task 5"),
            ft.Text("Task 6"),
            ft.Text("Task 7"),
            ft.Text("Task 8"),
            # ft.Text("Task 9"),
            # ft.Text("Task 10"),
            # ft.Text("Task 11"),
            # ft.Text("Task 12"),
        ],
    )
    items_left = ft.Text("0 items left")
    return ft.Column(
        expand=True,
        controls=[
            ft.Row(
                [ft.Text(value="Todos", style="headlineMedium")],
                alignment="center",
            ),
            ft.Row(
                controls=[
                    new_task,
                    ft.FloatingActionButton(
                        icon=ft.icons.ADD,
                        # on_click=self.add_clicked
                    ),
                ],
            ),
            filter,
            tasks,
            ft.Row(
                alignment="spaceBetween",
                # vertical_alignment="center",
                controls=[
                    items_left,
                    ft.OutlinedButton(
                        text="Clear completed",
                        # on_click=self.clear_clicked,
                    ),
                ],
            ),
            # ft.Column(
            #     spacing=25,
            #     controls=[
            #         # self.filter,
            #         # self.tasks,
            #         tasks,
            #         ft.Row(
            #             alignment="spaceBetween",
            #             # vertical_alignment="center",
            #             controls=[
            #                 # self.items_left,
            #                 ft.OutlinedButton(
            #                     text="Clear completed",
            #                     # on_click=self.clear_clicked,
            #                 ),
            #             ],
            #         ),
            #     ],
            # ),
        ],
    )


def main(page: ft.Page):
    page.title = "Flet to_do example"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(example())


if __name__ == "__main__":
    ft.app(target=main)
