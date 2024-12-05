import flet as ft


class PropertiesTable(ft.DataTable):
    def __init__(self, rows):
        super().__init__(
            columns=[
                ft.DataColumn(ft.Text("Property name", weight=ft.FontWeight.BOLD)),
                ft.DataColumn(
                    ft.Text("Property value", weight=ft.FontWeight.BOLD, width=200)
                ),
            ]
        )
        self.rows = rows

    def get_value_control(self, value_type, value, value_changed, data):
        match value_type:
            case "text":
                return ft.TextField(
                    content_padding=3,
                    value=value,
                    data=data,
                    on_change=value_changed,
                )
            case "bool":
                return ft.Checkbox(value=value, data=data, on_change=value_changed)
            case "enum":
                return ft.Dropdown()

            # If an exact match is not confirmed, this last case will be used if provided
            case _:
                return ft.Text("Something's wrong with the type")
