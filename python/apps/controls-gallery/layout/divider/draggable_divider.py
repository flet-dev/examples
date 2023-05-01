import flet as ft

name = "Draggable Divider example"

def example():

    def move_divider(e: ft.DragUpdateEvent):
        c.height += e.delta_y
        c.update()

    c = ft.Container(
                bgcolor=ft.colors.AMBER,
                alignment=ft.alignment.center,
                height=100,
                #expand=1,
            )

    return ft.Column(
            [
                c,
                ft.GestureDetector(
                    content=ft.Divider(),
                    on_pan_update=move_divider),
                ft.Container(bgcolor=ft.colors.PINK, alignment=ft.alignment.center, expand=1),],
            spacing=0,
            width=400,
            height=400)