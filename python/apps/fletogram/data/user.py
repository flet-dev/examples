import flet as ft

from utils.generate_avatar import get_avatar_color, get_initials


class Organization:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.members = []


class User(ft.ListTile):
    def __init__(self, id, display_name, first_name=None, last_name=None, avatar=None):
        super().__init__()
        self.adaptive = (True,)
        self.id = id
        self.display_name = display_name
        self.first_name = first_name
        self.last_name = last_name
        self.title = ft.Text(display_name)
        self.leading = ft.CircleAvatar(
            content=ft.Text(get_initials(self.display_name)),
            foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
            color=ft.colors.WHITE,
            bgcolor=get_avatar_color(self.display_name),
        )
