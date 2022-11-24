import logging
import flet
from flet import (
    Page,
    DragTarget,
    Draggable,
    Container,
    Column,
    Row,
    Text,
    TextButton,
    Icon,
    TextField,
    UserControl,
    Card,
    icons,
    border_radius,
    border,
    alignment,
    colors,
    padding,
)


class OuterContainer(UserControl):

    def __init__(self, page, color):
        super().__init__()
        self.page = page
        self.container_color = color
        self.inners = Column([], tight=True, spacing=5)
        self.new_inner = InnerContainer(self)
        self.inners.controls.append(self.new_inner.view)

    def build(self):
        self.view = Draggable(
            group="outer",
            content=DragTarget(
                group="inner",
                content=DragTarget(
                    group="outer",
                    content=Container(
                        # expand=False,
                        content=InnerContainer(self).view,
                        width=200,
                        height=200,
                        bgcolor=self.container_color,
                        border_radius=5,
                        border=border.all(2, colors.BLACK12),
                    ),
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
        print("lists_drag_accept: ", e)
        src = self.page.get_control(e.src_id)

        # self.update()
        self.page.update()

    def drag_will_accept(self, e):
        print("lists_drag_will_accept: ", e)
        self.page.update()

    def drag_leave(self, e):
        print("lists_drag_leave: ", e)
        self.page.update()

    def inner_drag_accept(self, e):
        print("items_drag_accept: ", e)
        src = self.page.get_control(e.src_id)

        self.update()

    def inner_drag_will_accept(self, e):
        print("items_will_drag_accept: ", e)

        self.update()

    def inner_drag_leave(self, e):
        print("items_drag_leave: ", e)

        self.update()


class InnerContainer():

    def __init__(self, outer: OuterContainer):
        self.outer = outer
        self.control = Row([Container(
            width=50,
            height=50,
            expand=False,
            content=Row([Text("Drag Me!!")], width=50, height=50),
            bgcolor=colors.BLUE_GREY,
            border_radius=5,
            alignment=alignment.center
        )]
        )
        self.view = Draggable(
            group="inner",
            content=DragTarget(
                group="inner",
                content=self.control,

                on_accept=self.drag_accept,
                on_leave=self.drag_leave,
                on_will_accept=self.drag_will_accept,
            ),
            data=self
        )

    def drag_accept(self, e):
        # this is the item picked up (Draggable control)
        src = self.outer.page.get_control(e.src_id)

        # e.control is the DragTarget, i.e. This (self) Item in the list
        # skip if item is dropped on itself
        if (src.content.content == e.control.content):
            e.control.content.elevation = 1
            self.list.set_indicator_opacity(self.view, 0.0)
            e.control.update()
            return

        # item dropped within same list but not on self
        if (src.data.list == self.list):
            self.outer.add_item(chosen_control=src,
                                swap_control=self.view)
            self.outer.set_indicator_opacity(self.view, 0.0)
            e.control.content.elevation = 1
            e.control.update()
            return

        # item added to different list
        self.outer.add_item(src.data.inner_text, swap_control=self.view)
        # remove from the list to which draggable belongs
        src.data.list.remove_item(src)
        self.outer.set_indicator_opacity(self.view, 0.0)
        e.control.content.elevation = 1
        e.control.update()

    def drag_will_accept(self, e):
        self.list.set_indicator_opacity(self.view, 1.0)
        e.control.content.elevation = 20 if e.data == "true" else 1
        e.control.update()

    def drag_leave(self, e):
        self.list.set_indicator_opacity(self.view, 0.0)
        e.control.content.elevation = 1
        e.control.update()


def main(page: Page):

    page.title = "Drag and drop ordering"
    page.containers = Row([
        OuterContainer(page, colors.DEEP_ORANGE_400),
        OuterContainer(page, colors.PINK_400),
        OuterContainer(page, colors.CYAN_400),
    ], alignment="spaceAround", vertical_alignment="center", expand=True)
    page.add(page.containers)


#print("flet version: ", flet.version.version)
print("flet path: ", flet.__file__)
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s.%(msecs)03d %(message)s', datefmt='%H:%M:%S')
flet.app(target=main)
