import flet as ft

name = "Draggable VerticalDivider"


def example():
    async def move_vertical_divider(e: ft.DragUpdateEvent):
        if (e.delta_x > 0 and c.width < 300) or (e.delta_x < 0 and c.width > 100):
            c.width += e.delta_x
        await c.update_async()

    async def show_draggable_cursor(e: ft.HoverEvent):
        e.control.mouse_cursor = ft.MouseCursor.RESIZE_LEFT_RIGHT
        await e.control.update_async()

    c = ft.Container(
        bgcolor=ft.colors.ORANGE_300,
        alignment=ft.alignment.center,
        width=100,
        # expand=1,
    )

    return ft.Row(
        controls=[
            c,
            ft.GestureDetector(
                content=ft.VerticalDivider(),
                drag_interval=10,
                on_pan_update=move_vertical_divider,
                on_hover=show_draggable_cursor,
            ),
            ft.Container(
                bgcolor=ft.colors.BROWN_400,
                alignment=ft.alignment.center,
                expand=1,
            ),
        ],
        spacing=0,
        width=400,
        height=400,
    )
