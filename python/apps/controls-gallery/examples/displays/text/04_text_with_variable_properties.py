import flet as ft

from components.properties_table import PropertiesTable

name = "Text with variable properties"


def example():

    def get_source_code():

        code = f"""text_control = ft.Text(value="{t.value}", italic={t.italic}, selectable={t.selectable}, size={t.size})"""
        return code

    def update_example():
        source_code.value = get_source_code()
        example_control.update()

    def value_changed(e):
        t.value = e.control.value
        update_example()

    def italic_changed(e):
        t.italic = e.control.value
        update_example()

    def selectable_changed(e):
        t.selectable = e.control.value
        update_example()

    def size_changed(e):
        t.size = e.control.value
        update_example()

    t = ft.Text(value="This is a sample text", italic=True, selectable=True, size=20)

    size_dropdown = ft.Dropdown(
        content_padding=3,
        value=t.size,
        options=[
            ft.dropdown.Option("12"),
            ft.dropdown.Option("14"),
            ft.dropdown.Option("16"),
            ft.dropdown.Option("18"),
        ],
        on_change=size_changed,
    )

    properties_list = [
        {"name": "value", "value_type": "text"},
        {"name": "italic", "value_type": "bool"},
        {"name": "selectable", "value_type": "bool"},
        {"name": "size", "value_type": "text"},
    ]

    data_rows = []

    properties = PropertiesTable(rows=[])

    for property in properties_list:
        data_rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(property["name"])),
                    # ft.DataCell(
                    #     ft.TextField(
                    #         value=getattr(t, property), on_change=selectable_changed
                    #     )
                    # ),
                    ft.DataCell(
                        properties.get_value_control(
                            value_type=property["value_type"],
                            value=getattr(t, property["name"]),
                        )
                    ),
                ],
            ),
        )

    # properties = PropertiesTable(
    #     rows=[
    #         ft.DataRow(
    #             cells=[
    #                 ft.DataCell(ft.Text("value")),
    #                 ft.DataCell(
    #                     ft.TextField(
    #                         value=f"{t.value}",
    #                         on_change=value_changed,
    #                         content_padding=3,
    #                     )
    #                 ),
    #             ],
    #         ),
    #         ft.DataRow(
    #             cells=[
    #                 ft.DataCell(ft.Text("italic")),
    #                 ft.DataCell(ft.Checkbox(value=t.italic, on_change=italic_changed)),
    #             ],
    #         ),
    #         ft.DataRow(
    #             cells=[
    #                 ft.DataCell(ft.Text("selectable")),
    #                 ft.DataCell(
    #                     ft.Checkbox(value=t.selectable, on_change=selectable_changed)
    #                 ),
    #             ],
    #         ),
    #         ft.DataRow(
    #             cells=[
    #                 ft.DataCell(ft.Text("size")),
    #                 ft.DataCell(size_dropdown),
    #             ],
    #         ),
    #     ],
    # )

    properties.rows = data_rows

    source_code = ft.Text(value=get_source_code(), selectable=True)

    example_control = ft.Column(
        controls=[
            t,
            properties,
            ft.Text("Source code:", weight=ft.FontWeight.BOLD),
            source_code,
        ]
    )

    return example_control
