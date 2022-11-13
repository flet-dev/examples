import flet

from flet import (Column, ElevatedButton, Text, alignment,
                  TextField, Page, Container, TextStyle,
                  Row, colors, alignment)


def main(page: Page):
    def add_text_box(_):
        text_field = TextField(
            label=f'Text Box {len(left_column.controls)}',
            label_style=TextStyle(color=colors.GREEN),
            color=colors.GREEN,
            value=len(left_column.controls),
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
        scroll_mode_text.value = left_column.scroll
        page.update()

    add_text_box_button = ElevatedButton("Add TextBox", on_click=add_text_box)
    remove_text_box_button = ElevatedButton("Remove TextBox", on_click=remove_text_box)
    scroll_change_button = ElevatedButton("Change Scroll Mode", on_click=change_scroll)

    scroll_mode = scroll_generator(
        [None, True, False, "none", "auto", "adaptive", "always", "hidden"])

    left_column = Column([Text("THIS IS COL 1", color=colors.RED_400)],
                         scroll=next(scroll_mode),
                         )
    left_container = Container(
        left_column,
        expand=True,
        margin=10,
        padding=10,
        bgcolor=colors.AMBER_100,
        border_radius=10,
        alignment=alignment.top_center
    )
    scroll_mode_text = Text(str(left_column.scroll))
    right_container = Container(
        Column(
            [add_text_box_button, remove_text_box_button,
             scroll_change_button, scroll_mode_text],
        ),
        margin=10,
        padding=10,
        bgcolor=colors.CYAN_500,
        border_radius=10,
        expand=True,
        alignment=alignment.top_center
    )

    row = Row([left_container, right_container], expand=True)
    page.add(row)


flet.app(name="Flow", target=main)