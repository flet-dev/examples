import flet
from flet import (
    Container,
    DragUpdateEvent,
    GestureDetector,
    MouseCursor,
    Page,
    Stack,
    colors,
    ElevatedButton,
    Text,
)

def main(page: Page):
    def on_pan_update(event: DragUpdateEvent):
        container.top = max(0, container.top + event.delta_y)
        container.left = max(0, container.left + event.delta_x)
        container.update()

    gesture_detector = GestureDetector(
        mouse_cursor=MouseCursor.BASIC,
        drag_interval=50,
        on_pan_update=on_pan_update,
    )
    container = Container(gesture_detector, bgcolor=colors.AMBER, width=50, height=50, left=0, top=0)

    def change_icon(event):
        mouse_cursor = next(mouse_cursors)
        gesture_detector.mouse_cursor = mouse_cursor
        gesture_detector.update()
        text.value = f"Mouse Cursor:  {gesture_detector.mouse_cursor}"
        text.update()

    def mouse_cursor_generator(m_list):
        while True:
            for i in m_list:
                yield i
    mouse_cursors = mouse_cursor_generator(list(MouseCursor))

    page.add(Stack([container], width=1000, height=500))
    page.add(ElevatedButton("Change mouse Cursor", on_click=change_icon))
    text = Text(f"Mouse Cursor:  {gesture_detector.mouse_cursor}")
    page.add(text)

flet.app(target=main)