from typing import List

import flet as ft


class SecondaryMenuWeb(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 150
        self.bgcolor = ft.colors.GREY_100
        self.mail_actions = [ft.Text("Inbox"), ft.Text("Starred"), ft.Text("Spam")]
        self.chat_actions: List[ft.Control] = [ft.Text("Chat1"), ft.Text("Chat2")]
        self.content = ft.Column(controls=self.chat_actions)


class WebLayout(ft.View):
    def __init__(self):
        super().__init__()
        self.nav_rail_destinations = [
            ft.NavigationRailDestination(
                label="Mail",
                icon=ft.icons.MAIL_OUTLINED,
            ),
            ft.NavigationRailDestination(
                label="Chat",
                icon=ft.icons.CHAT_BUBBLE_OUTLINE,
            ),
            ft.NavigationRailDestination(
                label="Meet",
                icon=ft.icons.VIDEO_CHAT_OUTLINED,
            ),
        ]
        self.open_menu_button = ft.IconButton(
            icon=ft.icons.MENU, on_click=self.open_close_secondary_menu
        )
        self.rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            # bgcolor=ft.colors.PRIMARY_CONTAINER,
            # extended=True,
            min_width=100,
            min_extended_width=400,
            leading=self.open_menu_button,
            expand=True,
            group_alignment=-0.9,
            destinations=self.nav_rail_destinations,
            on_change=self.nav_rail_changed,
        )
        self.compose_button = ft.FloatingActionButton(
            icon=ft.icons.CREATE, text="Compose"
        )
        self.secondary_menu = SecondaryMenuWeb()
        self.expand = True

        self.controls = [
            ft.Row(
                [
                    ft.Column(
                        controls=[
                            self.rail,
                        ],
                    ),
                    self.secondary_menu,
                    ft.Column(
                        [ft.Text("Body!")],
                        alignment=ft.MainAxisAlignment.START,
                        expand=True,
                    ),
                ],
                expand=True,
            )
        ]

    def nav_rail_changed(self, e):
        print(f"Selected action: {e.control.selected_index}")
        if e.control.selected_index == 0:
            print("Open Mail Menu")
        if e.control.selected_index == 1:
            print("Open Chat Menu")

    def open_close_secondary_menu(self, e):
        print("Open secondary menu or close secondary menu")
        self.secondary_menu.visible = not self.secondary_menu.visible
        self.update()
