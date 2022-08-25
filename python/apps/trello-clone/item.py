import flet
from flet import (
    Page,
    DragTarget,
    Draggable,
    Container,
    Checkbox,
    Column,
    Row,
    Text,
    TextButton,
    Icon,
    TextField,
    Card,
    icons,
    border_radius,
    border,
    alignment,
    colors,
    padding,
)


class Item():
    def __init__(self, list, item_text: str):
        self.list = list
        self.item_text = item_text
        # card for now but will switch to more flexible component
        self.card_item = Card(
            content=Container(
                content=Checkbox(label=f"{self.item_text}"),
                width=200,
                padding=7
            ),
            elevation=1,
            data=self.list
        )
        self.view = Draggable(
            group="lists",
            content=DragTarget(
                group="lists",
                content=self.card_item,
                on_accept=self.drag_accept,
                on_leave=self.drag_leave,
                on_will_accept=self.drag_will_accept,
            ),
            data=self

        )

    def drag_accept(self, e):
        # this is the item picked up (Draggable control)
        src = self.list.page.get_control(e.data)

        # e.control is the DragTarget, i.e. This (self) Item in the list
        # skip if item is dropped on itself
        if (src.content.content == e.control.content):
            e.control.content.elevation = 1
            self.list.set_indicator_opacity(self.view, 0.0)
            e.control.update()
            return

        # item dropped within same list but not on self
        if (src.data.list == self.list):
            self.list.add_item(chosen_control=src,
                               swap_control=self.view)
            e.control.update()
            return

        # item added to different list
        self.list.add_item(src.data.item_text, swap_control=self.view)
        # remove from the list to which draggable belongs
        src.data.list.remove_item(src)
        self.list.set_indicator_opacity(self.view, 0.0)
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
