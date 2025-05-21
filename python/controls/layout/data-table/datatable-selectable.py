import flet as ft


def main(page: ft.Page):
    def selection_change(e):
        print(f"selection_change called with {e.control.data}")
        match e.control.data:
            case 1:
                dr1.selected = not dr1.selected
            case 2:
                dr2.selected = not dr2.selected
            case 3:
                dr3.selected = not dr3.selected
        page.update()

    def sort(e):
        print(f"sort called with {e.control.data} {e.control}")
        match e.control.data:
            case 1:
                print(f"{e.column_index}, {e.ascending}")
                # dt.sort_column_index = 1
                dt.sort_ascending = e.ascending
            case 2:
                print(f"{e.column_index}, {e.ascending}")
                # dt.sort_column_index = 2
                dt.sort_ascending = e.ascending
        dt.update()
        page.update()

    dr1 = ft.DataRow(
        [ft.DataCell(ft.Text("A")), ft.DataCell(ft.Text("1"))],
        selected=True,
        on_select_changed=selection_change,
        data=1,
    )
    dr2 = ft.DataRow(
        [ft.DataCell(ft.Text("B")), ft.DataCell(ft.Text("2"))],
        selected=False,
        on_select_changed=selection_change,
        data=2,
    )
    dr3 = ft.DataRow(
        [ft.DataCell(ft.Text("C")), ft.DataCell(ft.Text("3"))],
        selected=False,
        on_select_changed=selection_change,
        data=3,
    )
    dc1 = ft.DataColumn(
        ft.Text("Column 1"),
        tooltip="This is the first column",
        data=1,
        on_sort=sort,
    )
    dc2 = ft.DataColumn(
        ft.Text("Column 2"),
        tooltip="This is a second column",
        numeric=True,
        data=2,
        on_sort=sort,
    )
    dt = ft.DataTable(
        width=700,
        bgcolor=ft.Colors.TEAL_ACCENT_200,
        border=ft.Border.all(2, ft.Colors.RED_ACCENT_200),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(3, ft.Colors.BLUE_600),
        horizontal_lines=ft.border.BorderSide(1, ft.Colors.GREEN_600),
        sort_column_index=0,
        sort_ascending=True,
        heading_row_color=ft.Colors.BLACK12,
        heading_row_height=100,
        data_row_color={ft.ControlState.HOVERED: "0x30FF0000"},
        show_checkbox_column=True,
        divider_thickness=0,
        column_spacing=200,
        columns=[dc1, dc2],
        rows=[dr1, dr2, dr3],
    )

    page.add(dt)


ft.run(target=main)
