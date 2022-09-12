from flet import (
    UserControl,
    Draggable,
    DragTarget,
    Column,
    Row,
    Switch,
    Checkbox,
    Text,
    FloatingActionButton,
    PopupMenuButton,
    PopupMenuItem,
    Container,
    TextButton,
    TextField,
    IconButton,
    Card,
    icons,
    border_radius,
    alignment,
    border,
    colors,
    padding,
    margin
)
from item import Item


class BoardList(UserControl):

    def __init__(self, board, title: str, color: str = ""):
        super().__init__()
        self.board = board
        self.title = title
        self.color = color

    def build(self):

        self.item_name = TextField(
            label="new card name", width=200, height=50, bgcolor=colors.WHITE)
        self.items = Column([], tight=True, spacing=4)
        self.end_indicator = Container(
            bgcolor=colors.BLACK26,
            border_radius=border_radius.all(30),
            height=3,
            width=200,
            opacity=0.0
        )
        self.edit_field = Row([
            TextField(value=self.title, width=120, height=50),
            TextButton(text="Save", on_click=self.save_title)
        ])
        self.header = Row(
            # alignment="spaceBetween",
            # spacing=150,
            controls=[
                Text(value=self.title, style="titleMedium",
                     text_align="left", overflow="clip"),
                Row([
                    PopupMenuButton(
                        items=[
                            PopupMenuItem(
                                text="Edit", icon=icons.CREATE_ROUNDED, on_click=self.edit_title),
                            PopupMenuItem(
                                text="Delete", icon=icons.DELETE_ROUNDED, on_click=self.delete_list)
                        ],
                        # expand=True
                    )
                ], expand=True, alignment="end")
            ],

        )

        self.view = DragTarget(
            group="lists",
            content=Container(
                content=Column([
                    self.header,
                    self.item_name,
                    TextButton("add card", icon=icons.ADD,
                               on_click=self.add_item_handler),
                    self.items,
                    self.end_indicator
                ], spacing=4, tight=True, data=self.title),
                width=250,
                border=border.all(2, colors.BLACK12),
                border_radius=border_radius.all(5),
                bgcolor=self.color if (
                    self.color != "") else colors.BACKGROUND,
                padding=padding.only(bottom=10, right=10, left=10, top=5)
            ),

            on_accept=self.drag_accept,
            on_will_accept=self.drag_will_accept,
            on_leave=self.drag_leave
        )

        return self.view

    def drag_accept(self, e):
        src = self.board.app.page.get_control(e.data)
        self.add_item(src.data.item_text)
        src.data.list.remove_item(src.data)
        self.end_indicator.opacity = 0.0
        self.view.update()

    def drag_will_accept(self, e):
        self.end_indicator.opacity = 1.0
        self.view.update()

    def drag_leave(self, e):
        self.end_indicator.opacity = 0.0
        self.view.update()

    def delete_list(self, e):
        self.board.remove_list(self, e)

    def edit_title(self, e):
        self.header.controls[0] = self.edit_field
        self.header.controls[1].controls[0].visible = False

        #self.header.controls[1].content.visible = False
        self.update()

    def save_title(self, e):
        self.title = self.edit_field.controls[0].value
        self.header.controls[0] = Text(
            value=self.title, style="titleMedium")
        self.header.controls[1].controls[0].visible = True
        #self.header.controls[1].content.visible = True
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
            print("rearrange: ", to_index, from_index)
            self.items.controls.insert(
                to_index, self.items.controls.pop(from_index))
            self.set_indicator_opacity(swap_control, 0.0)

        # insert (drag from other list to middle of this list)
        elif (to_index is not None):
            print("insert: ", to_index)
            new_item = Item(self, item)
            control_to_add.controls.append(new_item)
            self.items.controls.insert(to_index, control_to_add)

        # add new (drag from other list to end of this list, or use add item button)
        else:
            print("add new: ", item)
            new_item = new_item = Item(self, item) if item else Item(
                self, self.item_name.value)
            control_to_add.controls.append(new_item)
            self.items.controls.append(control_to_add)
            self.item_name.value = ""

        print("self.items: ", self.items.controls)
        self.view.update()
        self.page.update()

    def remove_item(self, item):
        print("item from remove_item: ", item)
        controls_list = [x.controls[1] for x in self.items.controls]
        print("controls_list: ", controls_list)
        del self.items.controls[controls_list.index(item)]
        self.view.update()

    def set_indicator_opacity(self, item, opacity):
        controls_list = [x.controls[1] for x in self.items.controls]
        self.items.controls[controls_list.index(
            item)].controls[0].opacity = opacity
        self.view.update()
