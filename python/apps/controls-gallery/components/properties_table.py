import flet as ft


class PropertiesTable(ft.DataTable):
    def __init__(self, properties, control):
        super().__init__(
            columns=[
                ft.DataColumn(ft.Text("Property name", weight=ft.FontWeight.BOLD)),
                ft.DataColumn(
                    ft.Text("Property value", weight=ft.FontWeight.BOLD, width=200)
                ),
            ]
        )
        self.rows = self.get_rows(properties, control)
        self.properties = properties
        self.control = control
        self.source_code = ft.Text()

    def did_mount(self):
        self.update_source_code()

    def update_source_code(self):
        text = ""
        for property in self.properties:
            text = (
                text + f"{property["name"]}={getattr(self.control, property["name"])}, "
            )
        code = f"""text_control = ft.Text({text})"""
        self.source_code.value = code
        self.source_code.update()

    def get_rows(self, properties, control):
        data_rows = []

        for property in properties:
            data_rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(property["name"])),
                        ft.DataCell(
                            self.get_value_control(
                                value_type=property["value_type"],
                                value=getattr(control, property["name"]),
                                data=property["name"],
                            )
                        ),
                    ],
                ),
            )
        return data_rows

    def value_changed(self, e):
        print("Value changed!")
        setattr(self.control, e.control.data, e.control.value)
        self.update_source_code()
        self.control.update()

    def get_value_control(self, value_type, value, data):
        match value_type:
            case "text":
                return ft.TextField(
                    content_padding=3,
                    value=value,
                    data=data,
                    on_change=self.value_changed,
                )
            case "bool":
                return ft.Checkbox(
                    value=value,
                    data=data,
                    on_change=self.value_changed,
                )
            case "enum":
                return ft.Dropdown()

            # If an exact match is not confirmed, this last case will be used if provided
            case _:
                return ft.Text("Something's wrong with the type")
