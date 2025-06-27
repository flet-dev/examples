import flet as ft


class OuterContainer(ft.Draggable):

    def __init__(self, color, list_ref: ft.Ref[ft.Row], inner_container):

        self.list_ref = list_ref
        self.container_color = color

        # inner_container is a draggable
        self.inner_container = inner_container
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
            group="outer",
            content=self.outer_container,
            data=self,
            on_accept=self.drag_accept,
            on_will_accept=self.drag_will_accept,
            on_leave=self.drag_leave,
        )
        super().__init__(content=self.target, group="outer", data=self)

    def drag_accept(self, e):
        print(f"drag_accept outer e: {e}")

        self.outer_container.border = ft.Border.all(4, ft.Colors.BLACK12)
        self.list_ref.current.controls[0], self.list_ref.current.controls[1] = (
            self.list_ref.current.controls[1],
            self.list_ref.current.controls[0],
        )
        self.list_ref.current.update()
        self.update()

    def drag_will_accept(self, e: ft.DragWillAcceptEvent):
        print(f"drag_will_accept outer e: {e}")
        if e.accept and e.control != self.parent:
            self.outer_container.border = ft.Border.all(8, ft.Colors.BLACK54)
        self.update()

    def drag_leave(self, e):
        print(f"drag_leave outer e: {e}")

        self.outer_container.border = ft.Border.all(4, ft.Colors.BLACK12)
        self.update()


class InnerContainer(ft.Draggable):

    # def __init__(self, outer: OuterContainer, list_ref, inner_color):
    def __init__(self, inner_color, id):

        self.inner_color = inner_color
        self.id = id
        self.data = id
        self.inner_icon = ft.Icon(
            ft.Icons.CIRCLE, color=inner_color, size=100, tooltip="drag me!"
        )

        self.target = ft.DragTarget(
            group="inner",
            content=self.inner_icon,
            on_accept=self.drag_accept,
            on_leave=self.drag_leave,
            on_will_accept=self.drag_will_accept,
            data=self.id,
        )
        super().__init__(
            content=self.target, group="inner", max_simultaneous_drags=1, data=self
        )

    def set_color(self, color: str):
        self.inner_icon.color = color
        self.update()

    def drag_accept(self, e: ft.DragTargetEvent):
        print(f"drag_accept inner e: {e}")
        # self.set_color(self.inner_color)
        control: InnerContainer = self.page.get_control(e.src_id)
        # print(f"control: {control}")
        # if self.inner_color == state.color1:
        #     self.set_color(state.color2)
        #     self.state.

        # else:
        #     self.set_color(state.color1)
        if control.inner_color == state.color1:
            print("Triggered 1")
            control.set_color(state.color2)
            self.set_color(state.color1)
        else:
            print("Triggered 2")
            control.set_color(state.color1)
            self.set_color(state.color2)
        # if self.inner_color == state.color1:
        #     state.inner1.set_color(state.inner2.inner_color)
        # state.inner1.set_color(state.inner2.inner_color)
        # state.inner2.set_color(state.inner1.inner_color)

        # (
        #     self.list_ref.current.controls[0].content.content.content,
        #     self.list_ref.current.controls[1].content.content.content,
        # ) = (
        #     self.list_ref.current.controls[1].content.content.content,
        #     self.list_ref.current.controls[0].content.content.content,
        # )
        # self.list_ref.current.update()
        self.update()
        # self.set_color(ft.Colors.WHITE54)

    def drag_will_accept(self, e: ft.DragWillAcceptEvent):
        print(f"drag_will_accept inner e: {e}")
        # print(
        #     f"e.accept and e.data = {e.data} and self.id = {self.id} and e.src_id = {e.src_id}"
        # )

        if e.accept:

            self.set_color(ft.Colors.GREEN_300)
        self.update()

    def drag_leave(self, e):
        print(f"drag_leave inner e: {e}")

        self.set_color(self.inner_color)
        self.update()


class State:
    color1: str = ft.Colors.BLACK
    color2: str = ft.Colors.WHITE
    inner1: InnerContainer = InnerContainer(ft.Colors.BLACK, "1")
    inner2: InnerContainer = InnerContainer(ft.Colors.WHITE, "2")


state = State()


def main(page: ft.Page):

    page.title = "Drag and drop ordering"
    list_ref = ft.Ref[ft.Row]()
    page.bgcolor = ft.Colors.BLUE_GREY_100
    page.add(
        ft.Row(
            [
                OuterContainer(
                    ft.Colors.DEEP_ORANGE_400, list_ref, inner_container=state.inner1
                ),
                OuterContainer(
                    ft.Colors.BLUE_400, list_ref, inner_container=state.inner2
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            ref=list_ref,
        )
    )
    page.update()


ft.run(main)
