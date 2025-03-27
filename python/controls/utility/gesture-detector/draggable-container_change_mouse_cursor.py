import flet as ft


def main(page: ft.Page):
    def on_pan_update(event: ft.DragUpdateEvent):
        c.top = max(0, c.top + event.delta_y)
        c.left = max(0, c.left + event.delta_x)
        c.update()

    gd = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.BASIC,
        drag_interval=50,
        on_pan_update=on_pan_update,
    )
    c = ft.Container(gd, bgcolor=ft.Colors.AMBER, width=50, height=50, left=0, top=0)

    def change_icon(event):
        mouse_cursor = next(mouse_cursors)
        gd.mouse_cursor = mouse_cursor
        gd.update()
        text.value = f"Mouse Cursor:  {gd.mouse_cursor}"
        text.update()

    def mouse_cursor_generator(m_list):
        while True:
            for i in m_list:
                yield i

    mouse_cursors = mouse_cursor_generator(list(ft.MouseCursor))

    page.add(ft.Stack([c], width=1000, height=500))
    page.add(ft.ElevatedButton("Change mouse Cursor", on_click=change_icon))
    text = ft.Text(f"Mouse Cursor:  {gd.mouse_cursor}")
    page.add(text)


ft.app(target=main)
