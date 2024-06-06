import flet as ft


class MailActionWeb(ft.Container):
    def __init__(self, text):
        super().__init__()
        self.bgcolor = ft.colors.GREY_100
        self.content = ft.Text(value=text)


class MailMenuWeb(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 150
        self.bgcolor = ft.colors.GREY_100
        self.content = ft.Column(
            controls=[MailActionWeb(text="Inbox"), MailActionWeb(text="Starred")]
        )


class MailMenuMobile(ft.NavigationDrawer):
    def __init__(self):
        super().__init__()
        # self.width = 150
        # self.bgcolor = ft.colors.GREY_100
        self.controls = [MailActionWeb(text="Inbox"), MailActionWeb(text="Starred")]
