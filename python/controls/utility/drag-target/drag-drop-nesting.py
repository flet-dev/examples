import logging
import flet
from flet import (
    Page,
    DragTarget,
    Draggable,
    Container,
    Column,
    Row,
    Icon,
    UserControl,
    icons,
    border,
    alignment,
    colors,
)


class OuterContainer(UserControl):

    def __init__(self, page, color):
        super().__init__()
        self.page = page
        self.container_color = color
        self.inner_container = InnerContainer(self)
        self.outer_container = Container(
            content=self.inner_container.view,
            width=200,
            height=200,
            bgcolor=self.container_color,
            border_radius=5,
            alignment=alignment.center,
            border=border.all(4, colors.BLACK12),
        )

    def build(self):
        self.view = Draggable(
            group="outer",
            content=DragTarget(
                group="inner",
                content=DragTarget(
                    group="outer",
                    content=self.outer_container,
                    data=self,
                    on_accept=self.drag_accept,
                    on_will_accept=self.drag_will_accept,
                    on_leave=self.drag_leave
                ),
                data=self,
                on_accept=self.inner_drag_accept,
                on_will_accept=self.inner_drag_will_accept,
                on_leave=self.inner_drag_leave
            )
        )
        return self.view

    def drag_accept(self, e):
        if e.data == 'true':
            self.outer_container.border = border.all(4, colors.BLACK12)
        self.view.update()

    def drag_will_accept(self, e):
        if e.data == 'true':
            self.outer_container.border = border.all(4, colors.BLACK54)
        self.view.update()

    def drag_leave(self, e):
        self.outer_container.border = border.all(4, colors.BLACK12)
        self.view.update()

    def inner_drag_accept(self, e):
        if e.data == 'true':
            self.outer_container.border_radius = 5
        self.update()

    def inner_drag_will_accept(self, e):
        if e.data == 'true':
            self.outer_container.border_radius = 25
        self.update()

    def inner_drag_leave(self, e):
        self.outer_container.border_radius = 5
        self.update()


class InnerContainer():

    def __init__(self, outer: OuterContainer):
        self.outer = outer
        self.inner_icon = Icon(
            icons.CIRCLE,
            color=colors.WHITE54,
            size=100,
            tooltip="drag me!"
        )

        self.view = Draggable(
            group="inner",
            content=DragTarget(
                group="inner",
                content=self.inner_icon,

                on_accept=self.drag_accept,
                on_leave=self.drag_leave,
                on_will_accept=self.drag_will_accept,
            ),
            data=self
        )

    def change_color(self, color: str):
        self.inner_icon.color = color
        self.view.update()

    def drag_accept(self, e):
        if e.data == 'true':
            self.change_color(colors.WHITE54)
        print("inner_drag_accept")

    def drag_will_accept(self, e):
        if e.data == "true":
            self.change_color(colors.BLUE_GREY)
        self.view.update()

    def drag_leave(self, e):
        self.change_color(colors.WHITE54)
        self.view.update()


def main(page: Page):

    page.title = "Drag and drop ordering"
    page.bgcolor = colors.BLUE_GREY_100
    page.containers = Row([
        OuterContainer(page, colors.DEEP_ORANGE_400),
        OuterContainer(page, colors.BLUE_400),
    ], alignment="spaceAround", vertical_alignment="center", expand=True)
    page.add(page.containers)


# print("flet path: ", flet.__file__)
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s.%(msecs)03d %(message)s', datefmt='%H:%M:%S')
flet.app(target=main)
