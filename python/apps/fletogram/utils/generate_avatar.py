import flet as ft


def get_initials(user_name: str):
    if user_name:
        return user_name[:1].capitalize()
    else:
        return "Unknown"  # or any default value you prefer


def get_avatar_color(user_name: str):
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
