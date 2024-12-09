import flet as ft

from components.properties_table import PropertiesTable

name = "Text with variable properties"


def example():

    t = ft.Text(
        value="This is a sample text",
        italic=True,
        selectable=True,
        size=20,
        color=ft.Colors.GREEN_800,
        bgcolor=ft.Colors.GREEN_100,
        max_lines=2,
        style=ft.TextStyle(size=30),
    )

    style_properties_list = [
        {"name": "size", "value_type": "number"},
        {"name": "letter_spacing", "value_type": "number"},
    ]

    properties_list = [
        {
            "name": "value",
            "value_type": "str",
            "value": "This is the Text value provided in dict",
        },
        {"name": "italic", "value_type": "bool"},
        {"name": "selectable", "value_type": "bool"},
        {"name": "size", "value_type": "number"},
        {"name": "color", "value_type": "enum", "values": ft.Colors},
        {"name": "bgcolor", "value_type": "enum", "values": ft.Colors},
        {"name": "max_lines", "value_type": "number"},
        {
            "name": "style",
            "value_type": "dataclass",
            "properties": style_properties_list,
        },
    ]

    properties = PropertiesTable(properties_list, t)

    # source_code = ft.Text(value=get_source_code(), selectable=True)
    source_code = properties.source_code

    example_control = ft.Column(
        controls=[
            t,
            properties,
            ft.Text("Source code:", weight=ft.FontWeight.BOLD),
            source_code,
        ]
    )

    return example_control
