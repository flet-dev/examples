import flet as ft

name = "Draggable Divider example"


def example():
    async def move_divider(e: ft.DragUpdateEvent):
        if (e.delta_y > 0 and c.height < 300) or (e.delta_y < 0 and c.height > 100):
            c.height += e.delta_y
        await c.update_async()

    async def show_draggable_cursor(e: ft.HoverEvent):
        e.control.mouse_cursor = ft.MouseCursor.RESIZE_UP_DOWN
        await e.control.update_async()

    c = ft.Container(
        bgcolor=ft.colors.AMBER,
        alignment=ft.alignment.center,
        height=100,
        # expand=1,
    )

    return ft.Column(
        [
            c,
            ft.GestureDetector(
                content=ft.Divider(),
                on_pan_update=move_divider,
                on_hover=show_draggable_cursor,
            ),
            ft.Container(
                bgcolor=ft.colors.PINK, alignment=ft.alignment.center, expand=1
            ),
        ],
        spacing=0,
        width=400,
        height=400,
    )
