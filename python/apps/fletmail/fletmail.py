import flet as ft


class MainAction:
    def __init__(self, label, icon, on_click=None) -> None:
        self.label = label
        self.icon = icon
        self.on_click = on_click


class FletMail:
    def __init__(self) -> None:
        self.create_actions()
        self.open_close_menu = MainAction(
            label="Menu", icon=ft.icons.MENU, on_click=self.secondary_menu_clicked
        )

    def create_actions(self):
        action1 = MainAction(
            label="Mail",
            icon=ft.icons.MAIL_OUTLINED,
            on_click=self.action1_clicked,
        )
        action2 = MainAction(
            label="Chat",
            icon=ft.icons.CHAT_BUBBLE_OUTLINE,
            on_click=self.action2_clicked,
        )
        action3 = MainAction(
            label="Meet",
            icon=ft.icons.VIDEO_CHAT_OUTLINED,
            on_click=self.action3_clicked,
        )
        self.actions = [action1, action2, action3]

    def action1_clicked(self):
        print("Action1 clicked")

    def action2_clicked(self):
        print("Action2 clicked")

    def action3_clicked(self):
        print("Action3 clicked")

    def secondary_menu_clicked(self):
        print("Secondary Menu Clicked")

    def compose_action(self):
        print("Compose!")
