import flet as ft

name = "Drag and drop colors"


def example():
    async def drag_will_accept(e):
        e.control.content.border = ft.border.all(
            2, ft.colors.BLACK45 if e.data == "true" else ft.colors.RED
        )
        await e.control.update_async()

    async def drag_accept(e: ft.DragTargetAcceptEvent):
        src = e.control.page.get_control(e.src_id)
        e.control.content.bgcolor = src.content.bgcolor
        e.control.content.border = None
        await e.control.update_async()

    async def drag_leave(e):
        e.control.content.border = None
        await e.control.update_async()

    return ft.Row(
        [
            ft.Column(
                [
                    ft.Draggable(
                        group="color",
                        content=ft.Container(
                            width=50,
                            height=50,
                            bgcolor=ft.colors.CYAN,
                            border_radius=5,
                        ),
                        content_feedback=ft.Container(
                            width=20,
                            height=20,
                            bgcolor=ft.colors.CYAN,
                            border_radius=3,
                        ),
                    ),
                    ft.Draggable(
                        group="color",
                        content=ft.Container(
                            width=50,
                            height=50,
                            bgcolor=ft.colors.YELLOW,
                            border_radius=5,
                        ),
                    ),
                    ft.Draggable(
                        group="color1",
                        content=ft.Container(
                            width=50,
                            height=50,
                            bgcolor=ft.colors.GREEN,
                            border_radius=5,
                        ),
                    ),
                ]
            ),
            ft.Container(width=100),
            ft.DragTarget(
                group="color",
                content=ft.Container(
                    width=50,
                    height=50,
                    bgcolor=ft.colors.BLUE_GREY_100,
                    border_radius=5,
                ),
                on_will_accept=drag_will_accept,
                on_accept=drag_accept,
                on_leave=drag_leave,
            ),
        ]
    )
