import itertools
from flet import (
    UserControl,
    Draggable,
    DragTarget,
    Column,
    Row,
    Text,
    Icon,
    PopupMenuButton,
    PopupMenuItem,
    Container,
    TextButton,
    TextField,
    icons,
    border_radius,
    alignment,
    border,
    colors,
    padding,
    margin
)
from item import Item
from memory_store import store
from data_store import DataStore


class BoardList(UserControl):
    id_counter = itertools.count()

    def __init__(self, board, title: str, color: str = ""):
        super().__init__()
        self.board_list_id = next(BoardList.id_counter)
        self.store: DataStore = store
        self.board = board
        self.title = title
        self.color = color
        self.items = Column([], tight=True, spacing=4)
        self.items.controls = self.store.get_items(self.board_list_id)

    def build(self):

        self.item_name = TextField(
            label="new card name", height=50, bgcolor=colors.WHITE)

        self.end_indicator = Container(
            bgcolor=colors.BLACK26,
            border_radius=border_radius.all(30),
            height=3,
            width=200,
            opacity=0.0
        )
        self.edit_field = Row([
            TextField(value=self.title, width=150, height=40,
                      content_padding=padding.only(left=10, bottom=10)),
            TextButton(text="Save", on_click=self.save_title)
        ])
        self.header = Row(
            controls=[
                Text(value=self.title, style="titleMedium",
                     text_align="left", overflow="clip", expand=True),

                Container(
                    PopupMenuButton(
                        items=[
                            PopupMenuItem(
                                content=Text(value="Edit", style="labelMedium",
                                             text_align="center", color=self.color),
                                text="Edit", icon=icons.CREATE_ROUNDED, on_click=self.edit_title),
                            PopupMenuItem(),
                            PopupMenuItem(
                                content=Text(value="Delete", style="labelMedium",
                                             text_align="center", color=self.color),
                                text="Delete", icon=icons.DELETE_ROUNDED, on_click=self.delete_list),
                            PopupMenuItem(),
                            PopupMenuItem(
                                content=Text(value="Move List", style="labelMedium",
                                             text_align="center", color=self.color))
                        ],
                    ),
                    padding=padding.only(right=-10)
                )
            ],
            alignment="spaceBetween"

        )

        self.view = Draggable(
            group="board",
            content=DragTarget(
                group="lists",
                content=DragTarget(
                    group="board",
                    content=Container(
                        content=Column([
                            self.header,
                            self.item_name,
                            TextButton(content=Row([Icon(icons.ADD), Text("add card", color=colors.BLACK38)], tight=True),
                                       on_click=self.add_item_handler),
                            self.items,
                            self.end_indicator
                        ], spacing=4, tight=True, data=self.title),
                        width=250,
                        border=border.all(2, colors.BLACK12),
                        border_radius=border_radius.all(5),
                        bgcolor=self.color if (
                            self.color != "") else colors.BACKGROUND,
                        padding=padding.only(
                            bottom=10, right=10, left=10, top=5)
                    ),
                    data=self,
                    on_accept=self.list_drag_accept,
                    on_will_accept=self.list_will_drag_accept,
                    on_leave=self.list_drag_leave
                ),
                data=self,
                on_accept=self.item_drag_accept,
                on_will_accept=self.item_will_drag_accept,
                on_leave=self.item_drag_leave
            )
        )

        return self.view

    def item_drag_accept(self, e):
        src = self.board.app.page.get_control(e.src_id)
        self.add_item(src.data.item_text)
        src.data.list.remove_item(src.data)
        self.end_indicator.opacity = 0.0
        self.view.update()

    def item_will_drag_accept(self, e):
        self.end_indicator.opacity = 1.0
        self.view.update()

    def item_drag_leave(self, e):
        self.end_indicator.opacity = 0.0
        self.view.update()

    def list_drag_accept(self, e):
        print("event from drag accept: ", e)
        src = self.board.app.page.get_control(e.src_id)
        l = self.board.board_lists
        to_index = l.index(e.control.data)
        from_index = l.index(src.content.data)
        l[to_index+1].opacity = 0.0
        l[to_index], l[from_index] = l[from_index], l[to_index]
        #print("current board_lists: ", l)
        self.board.view.update()
        #print("list_drag_accept: ", e.control.data, src.content.data)

    def list_will_drag_accept(self, e):
        to_index = self.board.board_lists.index(e.control.data)
        self.board.board_lists[to_index+1].opacity = 1.0
        self.board.view.update()

    def list_drag_leave(self, e):
        to_index = self.board.board_lists.index(e.control.data)
        self.board.board_lists[to_index+1].opacity = 0.0
        self.board.view.update()

    def delete_list(self, e):
        self.board.remove_list(self, e)

    def edit_title(self, e):
        self.header.controls[0] = self.edit_field
        self.header.controls[1].visible = False
        self.update()

    def save_title(self, e):
        self.title = self.edit_field.controls[0].value
        self.header.controls[0] = Text(value=self.title, style="titleMedium",
                                       text_align="left", overflow="clip", expand=True)

        self.header.controls[1].visible = True
        self.update()

    def add_item_handler(self, e):
        if self.item_name.value == "":
            return
        self.add_item()

    def add_item(self, item: str = None, chosen_control: Draggable = None, swap_control: Draggable = None):

        controls_list = [x.controls[1] for x in self.items.controls]
        to_index = controls_list.index(
            swap_control) if swap_control in controls_list else None
        from_index = controls_list.index(
            chosen_control) if chosen_control in controls_list else None
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
            #print("rearrange: ", to_index, from_index)
            self.items.controls.insert(
                to_index, self.items.controls.pop(from_index))
            self.set_indicator_opacity(swap_control, 0.0)

        # insert (drag from other list to middle of this list)
        elif (to_index is not None):
            #print("insert: ", to_index)
            new_item = Item(self, item)
            control_to_add.controls.append(new_item)
            self.items.controls.insert(to_index, control_to_add)

        # add new (drag from other list to end of this list, or use add item button)
        else:
            #print("add new: ", item)
            new_item = Item(self, item) if item else Item(
                self, self.item_name.value)
            control_to_add.controls.append(new_item)
            self.items.controls.append(control_to_add)
            self.store.add_item(self.board_list_id, new_item)
            self.item_name.value = ""

        #print("self.items: ", self.items.controls)
        self.view.update()
        self.page.update()

    def remove_item(self, item: Item):
        #print("item from remove_item: ", item)
        controls_list = [x.controls[1] for x in self.items.controls]
        #print("controls_list: ", controls_list)
        del self.items.controls[controls_list.index(item)]
        self.store.remove_item(self.board_list_id, item.item_id)
        self.view.update()

    def set_indicator_opacity(self, item, opacity):
        controls_list = [x.controls[1] for x in self.items.controls]
        self.items.controls[controls_list.index(
            item)].controls[0].opacity = opacity
        self.view.update()
