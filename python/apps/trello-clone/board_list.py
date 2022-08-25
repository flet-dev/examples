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
        self.items = Column([], tight=True, spacing=5)
        # self.card_list = []

    def build(self):

        def drag_accept(self, e):
            src = self.page.get_control(e.data)
            self.add_item(src.data.item_text)
            src.data.list.remove_item(src)
            self.end_indicator.opacity = 0.0
            self.view.update()

        def drag_will_accept(self, e):
            self.end_indicator.opacity = 1.0
            self.view.update()

        def drag_leave(self, e):
            self.end_indicator.opacity = 0.0
            self.view.update()

        edit_field = Row([
            TextField(label=self.title),
            TextButton(text="Save", on_click=save_title)
        ])
        self.header = Row(
            # alignment="spaceAround",
            # spacing=150,
            controls=[
                Text(value=self.title, style="titleMedium"),
                Row([
                    IconButton(
                        icon=icons.CREATE_OUTLINED,
                        tooltip="Edit List Title",
                        on_click=edit_title,
                    ),
                    IconButton(
                        icons.DELETE_OUTLINE,
                        tooltip="Delete List",
                        on_click=delete_list,
                    )
                ], alignment="end", tight=True)
            ]
        )

        self.view = DragTarget(
            group="lists",
            content=Container(
                content=Column([
                    self.header,
                    TextField(label="new card name", width=200,
                              height=50, bgcolor=colors.WHITE),
                    TextButton("add card", icon=icons.ADD,
                               on_click=add_item_handler),
                    self.items
                ], spacing=4, tight=True, data=self.title),
                border=border.all(2, colors.BLACK12),
                border_radius=border_radius.all(5),
                bgcolor=self.color if (
                    self.color != "") else colors.BACKGROUND,
                padding=padding.only(bottom=10, right=20, left=20)
            ),
            on_accept=drag_accept,
            on_will_accept=drag_will_accept,
            on_leave=drag_leave
        )

        return self.view

    def edit_title(e):
            self.header.controls[0] = edit_field
            self.header.controls[1].visible = False
            self.header.controls[2].visible = False
            self.update()

        def delete_list(e):
            self.board.remove_list(self, e)

        def save_title(e):
            self.title = edit_field.controls[0].value
            self.header.controls[0] = Text(
                value=self.title, style="titleMedium")
            self.header.controls[1].visible = True
            self.header.controls[2].visible = True
            self.update()

        def add_item_handler(e):
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
                control_to_add.controls.append(new_item.view)
                self.items.controls.insert(to_index, control_to_add)

            # add new (drag from other list to end of this list, or use add item button)
            else:
                print("add new: ", item)
                new_item = new_item = Item(self, item) if item else Item(
                    self, self.item_name.value)
                control_to_add.controls.append(new_item.view)
                self.items.controls.append(control_to_add)
                self.item_name.value = ""

            print("self.items: ", self.items.controls)
            self.view.update()
            self.page.update()

