import flet as ft


def main(page: ft.Page):
    def add_text_box(_):
        text_field = ft.TextField(
            label=f"Text Box {len(left_column.controls)}",
            label_style=ft.TextStyle(color=ft.colors.GREEN),
            color=ft.colors.GREEN,
            value=str(len(left_column.controls)),
        )
        left_column.controls.append(text_field)
        page.update()

    def remove_text_box(_):
        if left_column.controls:
            left_column.controls.pop()
        page.update()

    def scroll_generator(scroll_mode_list):
        while True:
            for scroll_mode in scroll_mode_list:
                yield scroll_mode

    def change_scroll(_):
        left_column.scroll = next(scroll_mode)
        scroll_mode_text.value = str(left_column.scroll)
        page.update()

    add_text_box_button = ft.ElevatedButton("Add TextBox", on_click=add_text_box)
    remove_text_box_button = ft.ElevatedButton(
        "Remove TextBox", on_click=remove_text_box
    )
    scroll_change_button = ft.ElevatedButton(
        "Change Scroll Mode", on_click=change_scroll
    )

    scroll_mode = scroll_generator(
        [
            None,
            ft.ScrollMode.AUTO,
            ft.ScrollMode.ADAPTIVE,
            ft.ScrollMode.ALWAYS,
            ft.ScrollMode.HIDDEN,
        ]
    )

    left_column = ft.Column(
        [ft.Text("THIS IS COL 1", color=ft.colors.RED_400)],
        scroll=next(scroll_mode),
    )
    left_container = ft.Container(
        left_column,
        expand=True,
        margin=10,
        padding=10,
        bgcolor=ft.colors.AMBER_100,
        border_radius=10,
        alignment=ft.alignment.top_center,
    )
    scroll_mode_text = ft.Text(str(left_column.scroll))
    right_container = ft.Container(
        ft.Column(
            [
                add_text_box_button,
                remove_text_box_button,
                scroll_change_button,
                scroll_mode_text,
            ],
        ),
        margin=10,
        padding=10,
        bgcolor=ft.colors.CYAN_500,
        border_radius=10,
        expand=True,
        alignment=ft.alignment.top_center,
    )

    row = ft.Row([left_container, right_container], expand=True)
    page.add(row)


ft.app(target=main)
