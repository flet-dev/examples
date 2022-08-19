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


class ItemList():
    def __init__(self, page, list_name, color):

        self.page = page
        self.list_name = list_name
        self.items = []
        self.new_item = TextField(label="new item name", width=200)
        self.view = DragTarget(
            group="list",
            content=Container(
                content=Column([
                    self.new_item,
                    TextButton(
                        "add item", icon=icons.ADD, on_click=self.add_item),
                    *self.items
                ]),
                border=border.all(2, colors.BLACK12),
                border_radius=border_radius.all(15),
                bgcolor=color,
                padding=padding.all(20)
            )
        )

    def add_item(self, e):
        new_item = Item(self, self.new_item.value)
        self.view.content.content.controls.append(new_item.view)
        self.items.append(new_item.view)
        self.page.update()
        self.view.update()


class Item():
    def __init__(self, list, item_text):
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
            elevation=1
        )
        self.view = Draggable(
            group="items",
            content=DragTarget(
                group="items",
                content=self.card_item,
                # content=Container(
                #     content=Row([
                #         Icon(name=icons.CIRCLE_OUTLINED),
                #         Text(value=f"{self.item_text}")
                #     ])
                # ),
                on_accept=self.drag_accept,
                on_leave=self.drag_leave,
                on_will_accept=self.drag_will_accept
            )
        )

    def drag_accept(self, e):
        # this is the item picked up
        src = self.list.page.get_control(e.data)
        print("src.content.content: ", src.content.content)
        # this is the drag target, i.e. Item in the list
        swap = copy.copy(e.control.content)
        print("swap: ", swap)
        e.control.content = copy.copy(src.content.content)
        src.content.content = swap
        e.control.update()
        # src.update

    def drag_will_accept(self, e):
        # e.control.content.elevation = 2 if e.data == "true" else 1

        # e.control.update()
        pass

    def drag_leave(self, e):
        # e.control.elevation = 1
        # e.control.update()
        pass


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
