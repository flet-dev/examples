from typing import List

import flet as ft
from new_message_view import NewMessageWebView


class WebView(ft.View):
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
            min_width=100,
            # width=100,
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
        self.compose_button = ft.FloatingActionButton(
            icon=ft.icons.CREATE, text="Compose", on_click=self.compose_clicked
        )
        self.mail_actions = ft.Column(
            [
                ft.TextButton("Inbox"),
                ft.TextButton("Starred"),
                ft.TextButton("Spam"),
            ]
        )
        self.chat_actions = ft.Column([ft.TextButton("Chat1"), ft.TextButton("Chat2")])
        self.secondary_menu = ft.Column([self.compose_button, self.mail_actions])

        self.expand = True

        self.controls = [
            ft.Row(
                [
                    ft.Column(
                        controls=[
                            self.rail,
                        ],
                    ),
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                self.secondary_menu,
                                ft.Column(
                                    controls=[
                                        ft.TextField(),
                                        ft.Container(
                                            content=ft.Text("Body!"),
                                            bgcolor=ft.colors.WHITE,
                                            expand=True,
                                        ),
                                    ],
                                ),
                            ]
                        ),
                        bgcolor=ft.colors.GREY_100,
                        expand=True,
                        padding=20,
                    ),
                ],
                expand=True,
            )
        ]

    def nav_rail_changed(self, e):
        print(f"Selected action: {e.control.selected_index}")
        if e.control.selected_index == 0:
            print("Open Mail Menu")
            self.secondary_menu.controls[1] = self.mail_actions
        if e.control.selected_index == 1:
            print("Open Chat Menu")
            self.secondary_menu.controls[1] = self.chat_actions
        self.update()

    def open_close_secondary_menu(self, e):
        print("Open secondary menu or close secondary menu")
        self.secondary_menu.visible = not self.secondary_menu.visible
        self.update()

    def compose_clicked(self, e):
        print("Open new message dialog")
        self.page.views.append(NewMessageWebView())
        self.page.update()
