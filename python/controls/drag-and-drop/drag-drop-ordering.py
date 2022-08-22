import logging
from tokenize import String
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
    colors,
    padding,
)

# logging.basicConfig(level=logging.INFO)


class ItemList():
    def __init__(self, page, list_name, color):

        self.page = page
        self.list_name = list_name
        self.items = Column([])
        self.item_name = TextField(label="new item name", width=200)
        self.view = DragTarget(
            group="list",
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
            )
        )

    def add_item_handler(self, e):
        self.add_item()

    def add_item(self, item: str = None):
        new_item = Item(self, item) if item else Item(
            self, self.item_name.value)
        self.items.controls.append(new_item.view)
        self.item_name.value = ""
        print("self.items: ", self.items.controls)
        self.page.update()
        self.view.update()

    def check_item(self, item):
        print("item: ", item)
        for c in self.items.controls:
            print("c.content: ", c.content)
            if c.content == item:
                return True
        return False

    def remove_item(self, item):
        print("item from remove_item: ", item)
        self.items.controls.remove(item)
        self.view.update()
        pass


class Item():
    def __init__(self, list: ItemList, item_text):
        self.list = list
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
                padding=10
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
                # data=self.item_text
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

        self.list.add_item(src.data.item_text)
        # remove from the list to which draggable belongs
        src.data.list.remove_item(src)
        e.control.content.elevation = 1
        e.control.update()
        # self.list.update()

    def drag_will_accept(self, e):
        # e.control == self.view.content(dragtarget)
        # therefore no way to check if target and draggable are the same control.
        e.control.content.elevation = 20 if e.data == "true" else 1
        e.control.update()

    def drag_leave(self, e):
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
