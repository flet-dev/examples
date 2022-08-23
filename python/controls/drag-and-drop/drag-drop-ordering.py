import logging
from tokenize import String
from turtle import bgcolor
import flet
import copy
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
    Card,
    icons,
    border_radius,
    border,
    alignment,
    colors,
    padding,
)

# logging.basicConfig(level=logging.INFO)
# print("flet version: ", flet.version.version)


class ItemList():
    def __init__(self, page, list_name, color):

        self.page = page
        self.list_name: str = list_name
        self.items_hash: dict[Draggable, int] = {}
        self.items = Column([
            Container(
                bgcolor=colors.BLACK26,
                # border=border.all(2, colors.BLACK26),
                border_radius=border_radius.all(30),
                height=3,
                width=200,
                opacity=0.0,
                data=-1
                # expand=True
            )
        ], spacing=1, tight=True)
        self.item_name = TextField(label="new item name", width=200)
        self.view = DragTarget(
            group="items",
            content=Container(
                content=Column([
                    self.item_name,
                    TextButton(
                        "add item", icon=icons.ADD, on_click=self.add_item_handler),
                    self.items
                ]),
                border=border.all(2, colors.BLACK12),
                border_radius=border_radius.all(15),
                bgcolor=color,
                padding=padding.all(20)
            ),
            on_will_accept=self.drag_accept,
            on_leave=self.drag_leave
        )

    def add_item_handler(self, e):
        self.add_item()

    def add_item(self, item: str = None, index: int = None):
        offset_length = len(self.items.controls) - 1
        new_item = Item(self, item, (offset_length)) if item else Item(
            self, self.item_name.value, (offset_length))
        # store new list item in dict with the list as key and the index as value
        self.items_hash[new_item.view] = index if index else offset_length
        controls_to_add = Column([
            Container(
                bgcolor=colors.BLACK26,
                border_radius=border_radius.all(30),
                height=3,
                alignment=alignment.center_right,
                width=200,
                opacity=0.0
            ),
            new_item.view
        ])

        # insert
        if (index):
            self.items.controls.insert(index, controls_to_add)
        # add new
        else:
            self.items.controls.insert(-1, controls_to_add)
        self.item_name.value = ""
        print("self.items: ", self.items.controls)
        self.page.update()
        self.view.update()

    def set_indicator_opacity(self, target, opacity):
        # print("target: ", target)
        # index = [x.content for x in self.items.controls].index(target)
        self.items.controls[target].controls[0].opacity = opacity
        self.view.update()

    def remove_item(self, item):

        # get the proper index from the hash as value
        del self.items.controls[self.items_hash[item]]
        self.view.update()

    def drag_accept(self, e):
        self.items.controls[-1].opacity = 1.0
        self.view.update()

    def drag_leave(self, e):
        self.items.controls[-1].opacity = 0.0
        self.view.update()


class Item():
    def __init__(self, list: ItemList, item_text: str, item_index: int):
        self.list = list
        self.item_index = item_index
        self.item_text = item_text
        self.card_item = Card(
            content=Container(
                content=Row([
                    Icon(name=icons.CIRCLE_OUTLINED),
                    Text(value=f"{self.item_text}")
                ],
                    alignment="start",
                ),
                width=200,
                padding=7
            ),
            elevation=1,
            data=self.list
        )
        self.view = Draggable(
            group="items",
            content=DragTarget(
                group="items",
                content=self.card_item,
                on_accept=self.drag_accept,
                on_leave=self.drag_leave,
                on_will_accept=self.drag_will_accept,
                # wy can't this be added to this component?
                # data=self.list
            ),
            data=self

        )

    def drag_accept(self, e):
        src = self.list.page.get_control(e.data)
        # this is the item picked up (Draggable control)
        print("src: ", src)

        # skip if item is dropped on itself
        if (src.content.content == e.control.content):
            e.control.content.elevation = 1
            e.control.update()
            return

        # this is the drag target, i.e. Item in the list (DragTarget)
        print("e.control: ", e.control)
        # index = [x.content for x in self.list.items.controls].index(e.control)
        print("self.item_index: ", self.item_index)
        self.list.add_item(src.data.item_text, self.item_index)
        # remove from the list to which draggable belongs
        src.data.list.remove_item(src)
        # self.list.set_indicator_opacity(e.control, 0.0)
        self.list.set_indicator_opacity(self.item_index, 0.0)
        e.control.content.elevation = 1
        e.control.update()
        # self.list.update()

    def drag_will_accept(self, e):
        # e.control == self.view.content(dragtarget)
        # therefore no way to check if target and draggable are the same control.
        self.list.set_indicator_opacity(self.item_index, 1.0)
        # self.list.set_indicator_opacity(e.control, 1.0)
        e.control.content.elevation = 20 if e.data == "true" else 1
        e.control.update()

    def drag_leave(self, e):
        # index = self.list.items.controls.index(self.view)
        # self.list.items.controls[index - 1].opacity = 0.0
        self.list.set_indicator_opacity(e.control, 0.0)
        e.control.content.elevation = 1
        e.control.update()


def main(page: Page):
    page.title = "Drag and drop ordering"

    page.add(

        Row([
            Column([
                ItemList(page, "List 1", colors.DEEP_ORANGE_400).view
            ]),
            Column([
                ItemList(page, "List 2", colors.PINK_400).view
            ]),
            Column([
                ItemList(page, "List 3", colors.CYAN_400).view
            ]),

        ])

    )


flet.app(target=main)
