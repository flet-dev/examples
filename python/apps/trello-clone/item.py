from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from board_list import BoardList
import itertools
from flet import (
    DragTarget,
    Draggable,
    Container,
    Checkbox,
    Column,
    Row,
    UserControl,
    Card,
    icons,
    border_radius,
    border,
    alignment,
    colors,
    padding,
)
#from main import app
from memory_store import store
from data_store import DataStore


class Item(UserControl):
    id_counter = itertools.count()

    def __init__(self, list: "BoardList", item_text: str):
        super().__init__()
        self.item_id = next(Item.id_counter)
        self.store: DataStore = store
        self.list = list
        self.item_text = item_text
        # card for now but will switch to more flexible component
        self.card_item = Card(
            content=Row(
                [Container(
                    content=Checkbox(label=f"{self.item_text}", width=200),
                    border_radius=border_radius.all(5))],
                width=200,
                # height=40,
                wrap=True
            ),
            elevation=1,
            data=self.list
        )

    def build(self):

        self.view = Draggable(
            group="items",
            content=DragTarget(
                group="items",
                content=self.card_item,
                on_accept=self.drag_accept,
                on_leave=self.drag_leave,
                on_will_accept=self.drag_will_accept,
            ),
            data=self
        )
        return self.view

    def drag_accept(self, e):
        src = self.page.get_control(e.src_id)

        # skip if item is dropped on itself
        if (src.content.content == e.control.content):
            print("skip")
            self.card_item.elevation = 1
            self.list.set_indicator_opacity(self, 0.0)
            e.control.update()
            return

        # item dropped within same list but not on self
        if (src.data.list == self.list):
            self.list.add_item(chosen_control=src.data,
                               swap_control=self)
            self.card_item.elevation = 1
            e.control.update()
            return

        # item added to different list
        self.list.add_item(src.data.item_text, swap_control=self)
        # remove from the list to which draggable belongs
        src.data.list.remove_item(src.data)
        self.list.set_indicator_opacity(self, 0.0)
        self.card_item.elevation = 1
        e.control.update()

    def drag_will_accept(self, e):
        self.list.set_indicator_opacity(self, 1.0)
        self.card_item.elevation = 20 if e.data == "true" else 1
        e.control.update()

    def drag_leave(self, e):
        self.list.set_indicator_opacity(self, 0.0)
        self.card_item.elevation = 1
        e.control.update()
