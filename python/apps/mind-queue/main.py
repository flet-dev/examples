import json
from pathlib import Path

import flet as ft

APP_NAME = "Mind Queue"
DATA_FILE = Path(__file__).resolve().parent / "data.json"


def load_data():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"{DATA_FILE} not found")
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def main(page: ft.Page):
    page.title = APP_NAME
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#111111"
    page.padding = ft.padding.symmetric(horizontal=24, vertical=24)
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = ft.ScrollMode.AUTO

    data = load_data()
    current_system: str | None = None

    # ---------- Dialog helpers ----------

    def close_current_dialog(e=None):
        changed = False
        for ctl in page.overlay:
            if isinstance(ctl, ft.AlertDialog) and ctl.open:
                ctl.open = False
                changed = True
        if changed:
            page.update()

    def open_dialog(dialog: ft.AlertDialog):
        if dialog not in page.overlay:
            page.overlay.append(dialog)
        dialog.open = True
        page.update()

    # ---------- System delete ----------

    def delete_system(system_name: str):
        nonlocal current_system
        if len(data.keys()) == 1:
            return
        data.pop(system_name, None)
        save_data(data)
        current_system = None
        show_dashboard()

    # ---------- Dashboard ----------

    def show_dashboard(e=None):
        nonlocal current_system
        current_system = None

        page.appbar = None
        page.clean()

        title = ft.Row(
            [ft.Text(APP_NAME, size=32, weight=ft.FontWeight.BOLD)],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        systems_list: list[ft.Control] = []

        def open_system(system_name: str):
            show_system(system_name)

        for system_name in data.keys():
            systems_list.append(
                ft.Container(
                    ft.Row([ft.Text(system_name, size=18, weight=ft.FontWeight.W_600)]),
                    padding=10,
                    margin=ft.margin.only(bottom=8),
                    border_radius=8,
                    bgcolor="#1c1c1c",
                    ink=True,
                    on_click=lambda e, n=system_name: open_system(n),
                )
            )

        # Add system dialog
        def open_add_system_dialog(e):
            name_field = ft.TextField(label="System name")

            def on_add(ev):
                name = name_field.value.strip()
                if not name:
                    return
                if name not in data:
                    data[name] = {}
                    save_data(data)
                close_current_dialog()
                show_dashboard()

            dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Add system"),
                content=name_field,
                actions=[
                    ft.TextButton("Cancel", on_click=close_current_dialog),
                    ft.TextButton("Add", on_click=on_add),
                ],
            )
            open_dialog(dlg)

        add_system_btn = ft.FilledButton(
            "Add system", icon=ft.Icons.ADD, on_click=open_add_system_dialog
        )

        page.add(
            ft.Column(
                [
                    title,
                    ft.Column(systems_list, spacing=4),
                    ft.Container(height=14),
                    add_system_btn,
                ],
                spacing=12,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        page.update()

    # ---------- System View ----------

    def show_system(system_name: str):
        nonlocal current_system
        current_system = system_name
        system_data: dict[str, list[list]] = data.get(system_name, {})

        # Edit system name
        def edit_system_name():
            name_field = ft.TextField(label="System name", value=system_name)

            def on_save(ev):
                new_name = name_field.value.strip()
                if not new_name or new_name == system_name or new_name in data:
                    close_current_dialog()
                    return

                data[new_name] = data.pop(system_name)
                save_data(data)
                close_current_dialog()
                show_system(new_name)

            dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Rename system"),
                content=name_field,
                actions=[
                    ft.TextButton("Cancel", on_click=close_current_dialog),
                    ft.TextButton("Save", on_click=on_save),
                ],
            )
            open_dialog(dlg)

        page.appbar = ft.AppBar(
            leading=ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=show_dashboard),
            title=ft.Text(system_name, size=32, weight=ft.FontWeight.BOLD),
            bgcolor=page.bgcolor,
            center_title=True,
            actions=[
                ft.IconButton(
                    icon=ft.Icons.EDIT,
                    tooltip="Rename",
                    on_click=lambda e: edit_system_name(),
                )
            ],
        )

        page.clean()
        content_controls: list[ft.Control] = []

        # ---------- Task Helpers ----------

        def toggle_task(section: str, index: int, value: bool):
            system_data[section][index][2] = value
            save_data(data)
            show_system(system_name)

        def delete_task(section: str, index: int):
            system_data[section].pop(index)
            save_data(data)
            show_system(system_name)

        def edit_task(section: str, index: int):
            title_val, label_val, done_val = system_data[section][index]
            title_field = ft.TextField(label="Title", value=title_val)
            label_field = ft.TextField(label="Task", value=label_val)

            def on_save(ev):
                t = title_field.value.strip()
                l = label_field.value.strip()
                if not t or not l:
                    return
                system_data[section][index][0] = t
                system_data[section][index][1] = l
                save_data(data)
                close_current_dialog()
                show_system(system_name)

            dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Edit task"),
                content=ft.Column([title_field, label_field], tight=True),
                actions=[
                    ft.TextButton("Cancel", on_click=close_current_dialog),
                    ft.TextButton("Save", on_click=on_save),
                ],
            )
            open_dialog(dlg)

        def add_task(section: str):
            title_field = ft.TextField(label="Title")
            label_field = ft.TextField(label="Task")

            def on_add(ev):
                t = title_field.value.strip()
                l = label_field.value.strip()
                if not t or not l:
                    return
                system_data.setdefault(section, []).append([t, l, False])
                save_data(data)
                close_current_dialog()
                show_system(system_name)

            dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text(f"Add task to {section}"),
                content=ft.Column([title_field, label_field], tight=True),
                actions=[
                    ft.TextButton("Cancel", on_click=close_current_dialog),
                    ft.TextButton("Add", on_click=on_add),
                ],
            )
            open_dialog(dlg)

        # ---------- Section Helpers ----------

        def delete_section(section: str):
            system_data.pop(section, None)
            save_data(data)
            show_system(system_name)

        def edit_section(section: str):
            name_field = ft.TextField(label="Header name", value=section)

            def on_save(ev):
                new_name = name_field.value.strip()
                if not new_name or new_name == section or new_name in system_data:
                    close_current_dialog()
                    return

                system_data[new_name] = system_data.pop(section)
                save_data(data)
                close_current_dialog()
                show_system(system_name)

            dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Rename header"),
                content=name_field,
                actions=[
                    ft.TextButton("Cancel", on_click=close_current_dialog),
                    ft.TextButton("Save", on_click=on_save),
                ],
            )
            open_dialog(dlg)

        def add_section():
            name_field = ft.TextField(label="Header name")

            def on_add(ev):
                name = name_field.value.strip()
                if not name:
                    return
                system_data[name] = []
                save_data(data)
                close_current_dialog()
                show_system(system_name)

            dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Add header"),
                content=name_field,
                actions=[
                    ft.TextButton("Cancel", on_click=close_current_dialog),
                    ft.TextButton("Add", on_click=on_add),
                ],
            )
            open_dialog(dlg)

        # ---------- Draw Sections + Tasks ----------

        for section_name, tasks in system_data.items():
            content_controls.append(ft.Container(height=10))

            # Header + delete/edit
            content_controls.append(
                ft.Row(
                    [
                        ft.Text(section_name, size=20, weight=ft.FontWeight.BOLD),
                        ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.Icons.EDIT,
                                    tooltip="Rename",
                                    on_click=lambda e, s=section_name: edit_section(s),
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.DELETE_OUTLINE,
                                    icon_color="red",
                                    tooltip="Delete",
                                    on_click=lambda e, s=section_name: delete_section(
                                        s
                                    ),
                                ),
                            ]
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )
            )

            for idx, (title_str, label, done) in enumerate(tasks):
                color = ft.Colors.WHITE70 if done else ft.Colors.WHITE
                deco = (
                    ft.TextDecoration.LINE_THROUGH if done else ft.TextDecoration.NONE
                )

                content_controls.append(
                    ft.Row(
                        [
                            ft.Checkbox(
                                value=done,
                                width=24,
                                height=24,
                                on_change=lambda e, s=section_name, i=idx: toggle_task(
                                    s, i, e.control.value
                                ),
                            ),
                            ft.Text(
                                title_str,
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=color,
                                style=ft.TextStyle(decoration=deco),
                            ),
                            ft.Container(width=8),
                            ft.Text(
                                label,
                                size=16,
                                color=color,
                                style=ft.TextStyle(decoration=deco),
                            ),
                            ft.Container(expand=True),
                            ft.IconButton(
                                icon=ft.Icons.EDIT_OUTLINED,
                                tooltip="Edit",
                                icon_size=18,
                                on_click=lambda e, s=section_name, i=idx: edit_task(
                                    s, i
                                ),
                            ),
                            ft.IconButton(
                                icon=ft.Icons.DELETE_OUTLINE,
                                icon_color="red",
                                tooltip="Delete",
                                icon_size=18,
                                on_click=lambda e, s=section_name, i=idx: delete_task(
                                    s, i
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=6,
                    )
                )

            # Add Task Button under section
            content_controls.append(
                ft.FilledButton(
                    "Add task",
                    icon=ft.Icons.ADD,
                    on_click=lambda e, s=section_name: add_task(s),
                )
            )

        # ---------- Add header + delete system bottom row ----------

        def confirm_delete_system():
            txt = ft.Text(
                f"Delete '{system_name}' permanently?\nThis cannot be undone."
            )

            def do_delete(ev):
                dlg.open = False
                page.update()
                delete_system(system_name)

            def do_cancel(ev):
                dlg.open = False
                page.update()

            dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Confirm delete"),
                content=txt,
                actions=[
                    ft.TextButton("Cancel", on_click=do_cancel),
                    ft.TextButton(
                        "Delete", icon=ft.Icons.DELETE_FOREVER, on_click=do_delete
                    ),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
            page.overlay.append(dlg)
            dlg.open = True
            page.update()

        content_controls.append(ft.Container(height=16))

        content_controls.append(
            ft.Row(
                [
                    ft.FilledButton(
                        "Add header",
                        icon=ft.Icons.ADD,
                        on_click=lambda e: add_section(),
                    ),
                    ft.FilledButton(
                        "Delete system",
                        icon=ft.Icons.DELETE_FOREVER,
                        bgcolor="red",
                        color="white",
                        on_click=lambda e: confirm_delete_system(),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        )

        page.add(ft.Column(content_controls, spacing=6, expand=True))
        page.update()

    # start at dashboard
    show_dashboard()


if __name__ == "__main__":
    ft.app(target=main)
