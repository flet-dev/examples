import flet as ft


class SecondaryAction(ft.Container):
    def __init__(self, text):
        super().__init__()
        self.bgcolor = ft.colors.GREY_100
        self.content = ft.Text(value=text)


class SecondaryMenuWeb(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 150
        self.bgcolor = ft.colors.GREY_100
        self.mail_actions = [
            SecondaryAction(text="Inbox"),
            SecondaryAction(text="Starred"),
        ]
        self.chat_actions = [
            SecondaryAction(text="Chat1"),
            SecondaryAction(text="Chat2"),
        ]
        self.meet_actions = [
            SecondaryAction(text="Meet1"),
            SecondaryAction(text="Meet2"),
        ]
        self.content = ft.Column(
            controls=[SecondaryAction(text="Inbox"), SecondaryAction(text="Starred")]
        )


class SecondaryMenuMobile(ft.NavigationDrawer):
    def __init__(self):
        super().__init__()
        # self.width = 150
        # self.bgcolor = ft.colors.GREY_100
        self.controls = [SecondaryAction(text="Inbox"), SecondaryAction(text="Starred")]
