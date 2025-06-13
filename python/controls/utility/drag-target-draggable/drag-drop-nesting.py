import flet as ft


class OuterContainer(ft.Draggable):

    def __init__(self, color, list_ref):

        self.list_ref = list_ref
        self.container_color = color
        # inner_container is a draggable
        self.inner_container = InnerContainer(self)
        self.outer_container = ft.Container(
            content=self.inner_container,
            width=200,
            height=200,
            bgcolor=self.container_color,
            border_radius=5,
            alignment=ft.Alignment.center(),
            border=ft.Border.all(4, ft.Colors.BLACK12),
        )

        self.target = ft.DragTarget(
            group="inner",
            content=ft.DragTarget(
                group="outer",
                content=self.outer_container,
                data=self,
                on_accept=self.drag_accept,
                on_will_accept=self.drag_will_accept,
                on_leave=self.drag_leave,
            ),
            data=self,
            on_accept=self.inner_drag_accept,
            on_will_accept=self.inner_drag_will_accept,
            on_leave=self.inner_drag_leave,
        )
        super().__init__(content=self.target, group="outer", data=self)

    def drag_accept(self, e):
        print(f"e: {e}")
        if e.data == "true":
            print("drag_accept outer")
            self.outer_container.border = ft.Border.all(4, ft.Colors.BLACK12)
        self.update()

    def drag_will_accept(self, e):
        print(f"e: {e}")
        if e.data == "true":
            print("drag_will_accept outer")
            self.outer_container.border = ft.Border.all(4, ft.Colors.BLACK54)
        self.update()

    def drag_leave(self, e):
        print(f"e: {e}")
        self.outer_container.border = ft.Border.all(4, ft.Colors.BLACK12)
        self.update()

    def inner_drag_accept(self, e):
        if e.data == "true":
            print("drag_accept inner")
            self.outer_container.border_radius = 5
        self.update()

    def inner_drag_will_accept(self, e):
        if e.data == "true":
            print("drag_will_accept inner")
            self.outer_container.border_radius = 25
        self.update()

    def inner_drag_leave(self, e):
        self.outer_container.border_radius = 5
        self.update()


class InnerContainer(ft.Draggable):

    def __init__(self, outer: OuterContainer):
        self.outer = outer
        self.inner_icon = ft.Icon(
            ft.Icons.CIRCLE, color=ft.Colors.WHITE54, size=100, tooltip="drag me!"
        )
        # self.data = self

        self.target = ft.DragTarget(
            group="inner",
            content=self.inner_icon,
            on_accept=self.drag_accept,
            on_leave=self.drag_leave,
            on_will_accept=self.drag_will_accept,
        )
        super().__init__(content=self.target, group="outer", data=self)

    def change_color(self, color: str):
        self.inner_icon.color = color
        self.update()

    def drag_accept(self, e):
        if e.data == "true":
            print("drag_accept from inner")
            self.change_color(ft.Colors.WHITE54)
        print("inner_drag_accept")

    def drag_will_accept(self, e):
        if e.data == "true":
            print("drag_will_accept from inner")
            self.change_color(ft.Colors.BLUE_GREY)
        self.update()

    def drag_leave(self, e):
        self.change_color(ft.Colors.WHITE54)
        self.update()


def main(page: ft.Page):

    page.title = "Drag and drop ordering"
    list_ref = ft.Ref[ft.Row]()
    page.bgcolor = ft.Colors.BLUE_GREY_100
    page.add(
        ft.Row(
            [
                OuterContainer(ft.Colors.DEEP_ORANGE_400, list_ref),
                OuterContainer(ft.Colors.BLUE_400, list_ref),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            ref=list_ref,
        )
    )
    page.update()


# print("flet path: ", flet.__file__)
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s.%(msecs)03d %(message)s', datefmt='%H:%M:%S')
ft.run(main)
