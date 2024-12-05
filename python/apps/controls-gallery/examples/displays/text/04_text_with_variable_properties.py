import flet as ft

from components.properties_table import PropertiesTable

name = "Text with variable properties"


def example():

    def get_source_code():
        text = ""
        for property in properties_list:
            text = text + f"{property["name"]}={getattr(t, property["name"])}, "
        code = f"""text_control = ft.Text({text})"""
        return code

    def update_example():
        source_code.value = get_source_code()
        example_control.update()

    t = ft.Text(value="This is a sample text", italic=True, selectable=True, size=20)

    properties_list = [
        {"name": "value", "value_type": "text"},
        {"name": "italic", "value_type": "bool"},
        {"name": "selectable", "value_type": "bool"},
        {"name": "size", "value_type": "text"},
    ]

    data_rows = []

    # properties = PropertiesTable(rows=data_rows)
    properties = PropertiesTable(properties_list, t)
    # for property in properties_list:
    #     data_rows.append(
    #         ft.DataRow(
    #             cells=[
    #                 ft.DataCell(ft.Text(property["name"])),
    #                 ft.DataCell(
    #                     properties.get_value_control(
    #                         value_type=property["value_type"],
    #                         value=getattr(t, property["name"]),
    #                         value_changed=value_changed,
    #                         data=property["name"],
    #                     )
    #                 ),
    #             ],
    #         ),
    #     )

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
