import flet as ft

name = "Text with variable properties"


def example():
    def get_text_style_options():
        options = []
        for style in ft.TextThemeStyle:
            options.append(ft.dropdown.Option(text=style.name, key=style.value))
        return options

    def get_source_code():
        if t.size == "":
            size = ""
        else:
            size = f"size={t.size}"

        if t.style == None:
            style = ""
        else:
            style = f"""style='{t.style}',"""

        code = f"""text_control = ft.Text(value="{t.value}", italic={t.italic}, selectable={t.selectable}, {style} {size})"""
        return code

    async def update_example():
        source_code.value = get_source_code()
        await example_control.update_async()

    async def value_changed(e):
        t.value = e.control.value
        await update_example()

    async def italic_changed(e):
        t.italic = e.control.value
        await update_example()

    async def selectable_changed(e):
        t.selectable = e.control.value
        await update_example()

    async def size_changed(e):
        t.size = e.control.value
        t.style = None
        style_dropdown.value = None
        await update_example()

    async def style_changed(e):
        t.size = None
        size_dropdown.value = None
        t.style = e.control.value
        await update_example()

    t = ft.Text(value="This is a sample text", size=12)

    text_style_options = get_text_style_options()

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

    style_dropdown = ft.Dropdown(
        content_padding=3,
        value=t.style,
        options=text_style_options,
        on_change=style_changed,
    )

    properties = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Property name", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(
                ft.Text("Property value", weight=ft.FontWeight.BOLD, width=200)
            ),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("value")),
                    ft.DataCell(
                        ft.TextField(
                            value=f"{t.value}",
                            on_change=value_changed,
                            content_padding=3,
                        )
                    ),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("italic")),
                    ft.DataCell(ft.Checkbox(value=t.italic, on_change=italic_changed)),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("selectable")),
                    ft.DataCell(
                        ft.Checkbox(value=t.selectable, on_change=selectable_changed)
                    ),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("size")),
                    ft.DataCell(size_dropdown),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("style")),
                    ft.DataCell(style_dropdown),
                ],
            ),
        ],
    )

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
