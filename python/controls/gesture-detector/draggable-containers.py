import flet
from flet import (
    Container,
    DragUpdateEvent,
    GestureDetector,
    MouseCursor,
    Page,
    Stack,
    colors,
)


def main(page: Page):
    def on_pan_update1(e: DragUpdateEvent):
        print(
            f"PAN UPDATE - dx: {e.delta_x}, dy: {e.delta_y}, gx: {e.global_x}, gy: {e.global_y}, lx: {e.local_x}, ly: {e.local_y}"
        )
        c.top = max(0, c.top + e.delta_y)
        c.left = max(0, c.left + e.delta_x)
        c.update()

    def on_pan_update2(e: DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()

    gd = GestureDetector(
        mouse_cursor=MouseCursor.MOVE,
        drag_interval=50,
        on_pan_start=lambda e: print(
            f"PAN START - gx: {e.global_x}, gy: {e.global_y}, lx: {e.local_x}, ly: {e.local_y}, kind: {e.kind}"
        ),
        on_pan_update=on_pan_update1,
        on_pan_end=lambda e: print(
            f"PAN END - pv: {e.primary_velocity}, vx: {e.velocity_x}, vy: {e.velocity_y}"
        ),
    )

    c = Container(gd, bgcolor=colors.AMBER, width=50, height=50, left=0, top=0)

    gd1 = GestureDetector(
        mouse_cursor=MouseCursor.MOVE,
        drag_interval=10,
        on_vertical_drag_update=on_pan_update2,
        left=100,
        top=100,
        content=Container(bgcolor=colors.BLUE, width=50, height=50),
    )

    page.add(Stack([c, gd1], width=1000, height=500))


flet.app(target=main)
