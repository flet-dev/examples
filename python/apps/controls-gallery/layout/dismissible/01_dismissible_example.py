import flet as ft

name = "Dismissible ListView Tiles"


def example():
    async def handle_dismiss(e):
        lv.controls.remove(e.control)
        await lv.update_async()

    def handle_update(e):
        print("update")

    def handle_resize(e):
        print("resize")

    lv = ft.ListView(
        controls=[
            ft.Dismissible(
                content=ft.ListTile(title=ft.Text(f"Item {i}")),
                dismiss_direction=ft.DismissDirection.HORIZONTAL,
                background=ft.Container(bgcolor=ft.colors.GREEN),
                secondary_background=ft.Container(bgcolor=ft.colors.RED),
                on_dismiss=handle_dismiss,
                on_update=handle_update,
                on_resize=handle_resize,
                dismiss_thresholds={
                    ft.DismissDirection.HORIZONTAL: 0.1,
                    ft.DismissDirection.START_TO_END: 0.1,
                },
            )
            for i in range(5)
        ]
    )

    return lv
