import flet as ft


def main(page: ft.Page):
    def get_options():
        icons = [
            {"name": "Smile", "icon_name": ft.Icons.SENTIMENT_SATISFIED_OUTLINED},
            {"name": "Cloud", "icon_name": ft.Icons.CLOUD_OUTLINED},
            {"name": "Brush", "icon_name": ft.Icons.BRUSH_OUTLINED},
            {"name": "Heart", "icon_name": ft.Icons.FAVORITE},
        ]
        return [
            ft.DropdownOption(key=icon["name"], leading_icon=icon["icon_name"])
            for icon in icons
        ]

    page.add(
        ft.Dropdown(
            border=ft.InputBorder.UNDERLINE,
            enable_filter=True,
            editable=True,
            leading_icon=ft.Icons.SEARCH,
            label="Icon",
            options=get_options(),
        )
    )


ft.run(main)
