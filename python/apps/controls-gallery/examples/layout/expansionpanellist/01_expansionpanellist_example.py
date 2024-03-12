import flet as ft

name = "ExpansionPanelList example"


def example():
    def handle_change(e: ft.ControlEvent):
        print(f"change on panel with index {e.data}")

    async def handle_delete(e: ft.ControlEvent):
        panel.controls.remove(e.control.data)
        await panel.update_async()

    panel = ft.ExpansionPanelList(
        expand_icon_color=ft.colors.AMBER,
        elevation=8,
        divider_color=ft.colors.AMBER,
        on_change=handle_change,
        controls=[
            ft.ExpansionPanel(
                # has no header and content - placeholders will be used
                bgcolor=ft.colors.BLUE_400,
                expanded=True,
            )
        ],
    )

    colors = [
        ft.colors.GREEN_500,
        ft.colors.BLUE_800,
        ft.colors.RED_800,
    ]

    for i in range(3):
        exp = ft.ExpansionPanel(
            bgcolor=colors[i % len(colors)],
            header=ft.ListTile(title=ft.Text(f"Panel {i}")),
        )

        exp.content = ft.ListTile(
            title=ft.Text(f"This is in Panel {i}"),
            subtitle=ft.Text(f"Press the icon to delete panel {i}"),
            trailing=ft.IconButton(ft.icons.DELETE, on_click=handle_delete, data=exp),
        )

        panel.controls.append(exp)

    return panel
