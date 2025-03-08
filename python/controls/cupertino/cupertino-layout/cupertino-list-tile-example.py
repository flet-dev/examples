import flet as ft


def main(page: ft.Page):
    def tile_clicked(e):
        print("Tile clicked")

    page.add(
        ft.CupertinoListTile(
            additional_info=ft.Text("Wed Jan 24"),
            bgcolor_activated=ft.Colors.AMBER_ACCENT,
            leading=ft.Icon(name=ft.CupertinoIcons.GAME_CONTROLLER),
            title=ft.Text("CupertinoListTile: notched = False"),
            subtitle=ft.Text("Subtitle"),
            trailing=ft.Icon(name=ft.CupertinoIcons.ALARM),
            on_click=tile_clicked,
        ),
        ft.CupertinoListTile(
            notched=True,
            additional_info=ft.Text("Thu Jan 25"),
            leading=ft.Icon(name=ft.CupertinoIcons.GAME_CONTROLLER),
            title=ft.Text("CupertinoListTile: notched = True"),
            subtitle=ft.Text("Subtitle"),
            trailing=ft.Icon(name=ft.CupertinoIcons.ALARM),
            on_click=tile_clicked,
        ),
    )


ft.app(main)
