import flet as ft


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
            content=ft.Text(self.get_initials(self.display_name)),
            color=ft.colors.WHITE,
            bgcolor=self.get_avatar_color(self.display_name),
        )

    def get_initials(self, user_name: str):
        if user_name:
            return user_name[:1].capitalize()
        else:
            return "Unknown"  # or any default value you prefer

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]
