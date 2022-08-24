import logging
from tokenize import String
from tracemalloc import start
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
        #self.items_hash: dict[Draggable, int] = {}
        self.items = Column([], tight=True, spacing=5)
        self.end_indicator = Container(
            bgcolor=colors.BLACK26,
            # border=border.all(2, colors.BLACK26),
            border_radius=border_radius.all(30),
            height=3,
            width=200,
            opacity=0.0,
            data=-1
        )
        self.item_name = TextField(
            label="New Item Name", width=200, height=50, filled=False, bgcolor=colors.WHITE24)
        self.view = DragTarget(
            group="items",
            content=Container(
                content=Column([
                    self.item_name,
                    TextButton(
                        "Add Item", icon=icons.ADD, on_click=self.add_item_handler),
                    self.items,
                    self.end_indicator
                ], spacing=4, tight=True),
                border=border.all(2, colors.BLACK12),
                border_radius=border_radius.all(15),
                bgcolor=color,
                padding=padding.all(20)
            ),
            on_accept=self.drag_accept,
            on_will_accept=self.drag_will_accept,
            on_leave=self.drag_leave
        )

    def add_item_handler(self, e):
        self.add_item()

    def add_item(self, item: str = None, chosen_control: Draggable = None, swap_control: Draggable = None):
        controls_list = [x.controls[1] for x in self.items.controls]
        to_index = controls_list.index(
            swap_control) if swap_control in controls_list else None
        from_index = controls_list.index(
            chosen_control) if chosen_control in controls_list else None
        #to_index = self.items_hash[swap_control] if swap_control else None
        #from_index = self.items_hash[chosen_control] if chosen_control else None
        control_to_add = Column([
            Container(
                bgcolor=colors.BLACK26,
                border_radius=border_radius.all(30),
                height=3,
                alignment=alignment.center_right,
                width=200,
                opacity=0.0
            )
        ])
        # rearrange (i.e. drag drop from same list)
        if ((from_index is not None) and (to_index is not None)):
            print("rearrange: ", to_index, from_index)
            #self.items_hash[self.items.controls[from_index]] = to_index
            #self.items_hash[self.items.controls[to_index]] = from_index
            self.items.controls.insert(
                to_index, self.items.controls.pop(from_index))
        # insert (drag from other list to middle of this list)
        elif (to_index is not None):
            print("insert: ", to_index)
            new_item = Item(self, item)
            control_to_add.controls.append(new_item.view)
            self.items.controls.insert(to_index, control_to_add)
        # add new (drag from other list to end of this list, or use add item button)
        else:
            print("add new: ", item)
            new_item = new_item = Item(self, item) if item else Item(
                self, self.item_name.value)
            control_to_add.controls.append(new_item.view)
            self.items.controls.append(control_to_add)

            #self.items_hash[new_item.view] = to_index if to_index else controls_length
            self.item_name.value = ""

        print("self.items: ", self.items.controls)
        self.view.update()
        self.page.update()

    def set_indicator_opacity(self, index, opacity):
        # print("target: ", target)
        # index = [x.content for x in self.items.controls].index(target)
        self.items.controls[index].controls[0].opacity = opacity
        self.view.update()

    def remove_item(self, item):
        #del self.items.controls[self.items_hash[item]]
        controls_list = [x.controls[1] for x in self.items.controls]
        del self.items.controls[controls_list.index(item)]
        self.view.update()

    def drag_accept(self, e):
        src = self.page.get_control(e.data)
        print("src: ", src, e.control.content)
        self.add_item(src.data.item_text)
        src.data.list.remove_item(src)
        self.end_indicator.opacity = 0.0
        self.view.update()

    def drag_will_accept(self, e):
        # self.items.controls[-1].opacity = 1.0
        print("self.end_indicator: ", self.end_indicator)
        self.end_indicator.opacity = 1.0
        self.view.update()

    def drag_leave(self, e):
        # self.items.controls[-1].opacity = 0.0
        self.end_indicator.opacity = 0.0
        self.view.update()


class Item():
    def __init__(self, list: ItemList, item_text: str):
        self.list = list
        # self.item_index = item_index
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

        # its dropped within same list but not on self
        if (src.data.list == self.list):
            self.list.add_item(chosen_control=src,
                               swap_control=self.view)
            # self.list.remove_item(src)
            e.control.update()
            return

        # this is the drag target, i.e. Item in the list (DragTarget)
        print("e.control: ", e.control)
        self.list.add_item(src.data.item_text, swap_control=self.view)
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
        self.list.set_indicator_opacity(self.item_index, 0.0)
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

        ], vertical_alignment="stretch")

    )


flet.app(target=main)
