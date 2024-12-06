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
        self.properties = properties
        self.control = control
        self.rows = self.get_rows()

        self.source_code = ft.Text()

    def did_mount(self):
        self.update_source_code()

    def update_source_code(self):
        text = ""
        for property in self.properties:
            if type(getattr(self.control, property["name"])).__name__ == "str":
                property_value = f"""'{getattr(self.control, property["name"])}'"""
            else:
                property_value = getattr(self.control, property["name"])
            text = text + f"{property["name"]}={property_value}, "
        control_name = type(self.control).__name__

        code = f"""ft.{control_name}({text})"""
        self.source_code.value = code
        self.source_code.update()

    def get_rows(self):
        data_rows = []

        for property in self.properties:

            print(
                f"Property type: {type(getattr(self.control, property["name"])).__name__}"
            )
            data_rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(property["name"])),
                        ft.DataCell(
                            # self.get_value_control(
                            #     value_type=property["value_type"],
                            #     value=getattr(self.control, property["name"]),
                            #     data=property["name"],
                            # )
                            self.get_value_control(property)
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

    # def get_value_control(self, value_type, value, data):
    def get_value_control(self, property):
        value = getattr(self.control, property["name"])
        match property["value_type"]:
            case "str":
                return ft.TextField(
                    content_padding=3,
                    value=value,
                    data=property["name"],
                    on_change=self.value_changed,
                )
            case "number":
                return ft.TextField(
                    content_padding=3,
                    value=value,
                    data=property["name"],
                    on_change=self.value_changed,
                )
            case "bool":
                return ft.Checkbox(
                    value=value,
                    data=property["name"],
                    on_change=self.value_changed,
                )
            case "enum":

                options = []

                options_list = property["values"]
                for item in options_list:
                    options.append(ft.dropdown.Option(item.value))

                return ft.Dropdown(
                    options=options,
                    value=value,
                    data=property["name"],
                    on_change=self.value_changed,
                )

            case "dataclass":

                return ft.Button(text="...")

            # If an exact match is not confirmed, this last case will be used if provided
            case _:
                return ft.Text("Something's wrong with the type")
