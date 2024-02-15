import flet as ft

from utils.generate_avatar import get_avatar_color, get_initials


class ContactTile(ft.ListTile):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.title = ft.Text(user.display_name)
        self.leading = ft.CircleAvatar(
            content=ft.Text(get_initials(self.user.display_name)),
            foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
            color=ft.colors.WHITE,
            bgcolor=get_avatar_color(self.user.display_name),
        )


class Contacts(ft.View):
    def __init__(self, fletogram):
        super().__init__()
        self.route = "/"
        self.appbar = ft.AppBar(
            leading=ft.TextButton("Edit"),
            title=ft.Text("Contacts"),
            actions=[
                ft.IconButton(icon=ft.icons.ADD_CARD),
            ],
        )
        self.fletogram = fletogram
        self.generate_contact_tiles()
        self.controls = [ft.ListView(spacing=5, controls=self.contact_tiles)]

        self.navigation_bar = self.fletogram.navigation_bar

    def generate_contact_tiles(self):
        self.contact_tiles = []
        for user in self.fletogram.users:
            self.contact_tiles.append(ContactTile(user))
