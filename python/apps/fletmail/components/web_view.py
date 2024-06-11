from typing import List

import flet as ft
from components.app_view import AppView
from components.new_message_view import NewMessageWebView
from model.messages import messages


class WebView(AppView):
    def __init__(self):
        super().__init__()
        self.logo = ft.Container(
            padding=5, content=ft.Image(src=f"logo.svg"), width=50, height=50
        )
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

        self.mail_menu = ft.Column([self.compose_button, self.mail_actions], width=150)
        self.chat_menu = ft.Column([self.compose_button, self.chat_actions], width=150)

        self.messages_list = ft.ListView(controls=self.get_messages(), expand=True)

        self.message_view = ft.Column(
            controls=[
                ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.back_to_messages),
                ft.Text(value="This is the email message"),
            ],
            visible=False,
        )

        self.mail_view = ft.Row(
            controls=[
                self.mail_menu,
                ft.Container(
                    content=ft.Column([self.messages_list, self.message_view]),
                    expand=True,
                    bgcolor=ft.colors.WHITE,
                ),
            ],
            expand=True,
        )

        self.chat_view = ft.Row(
            controls=[
                self.chat_menu,
                ft.Container(
                    content=ft.Text("Chat View"),
                    expand=True,
                    bgcolor=ft.colors.WHITE,
                ),
            ],
            expand=True,
            visible=False,
        )

        self.meet_view = ft.Container(
            content=ft.Text("Meet View"),
            expand=True,
            bgcolor=ft.colors.WHITE,
            visible=False,
        )

        self.controls = [
            ft.Row(
                [
                    ft.Column(
                        controls=[
                            self.rail,
                        ],
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        self.logo,
                                        ft.Text(
                                            "FletMail",
                                            width=100,
                                            style=ft.TextStyle(
                                                size=20, weight=ft.FontWeight.BOLD
                                            ),
                                        ),
                                        ft.TextField(),
                                    ]
                                ),
                                self.mail_view,
                                self.chat_view,
                                self.meet_view,
                                # self.message_view,
                            ],
                        ),
                        bgcolor=ft.colors.GREY_100,
                        expand=True,
                        padding=20,
                        margin=0,
                    ),
                ],
                expand=True,
            )
        ]

    def nav_rail_changed(self, e):
        print(f"Selected action: {e.control.selected_index}")
        if e.control.selected_index == 0:
            self.display_inbox()

        if e.control.selected_index == 1:
            self.display_chat()

        if e.control.selected_index == 2:
            self.display_meet()

        self.update()

    def open_close_secondary_menu(self, e):
        print("Open secondary menu or close secondary menu")
        self.mail_menu.visible = not self.mail_menu.visible
        self.chat_menu.visible = not self.chat_menu.visible
        self.update()

    def compose_clicked(self, e):
        print("Open new message dialog")
        self.page.views.append(NewMessageWebView())
        self.page.update()

    def get_messages(self):
        messages_list = []
        id = 1001
        for message in messages:
            message_title = message["title"]
            message_text = message["message"]
            messages_list.append(
                ft.ListTile(
                    data=id,
                    leading=ft.Checkbox(),
                    title=ft.Row(
                        controls=[
                            ft.Text(
                                message["author"],
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                                width=150,
                            ),
                            ft.Text(
                                value=f"{message_title}",
                                max_lines=1,
                                overflow=ft.TextOverflow.CLIP,
                            ),
                        ]
                    ),
                    trailing=ft.Text(value=message["date"]),
                    on_click=self.display_message,
                )
            )
            id += 1
        return messages_list

    def display_message(self, e):
        print("Message clicked!")
        self.messages_list.visible = False
        self.message_view.visible = True
        self.message_view.controls[1].value = e.control.data
        self.page.update()

    def back_to_messages(self, e):
        print("Go back to messages!")
        self.messages_list.visible = True
        self.message_view.visible = False
        # self.message_view.controls[1].value = e.control.data
        self.page.update()

    def display_inbox(self):
        print("Display inbox")
        self.mail_view.visible = True
        self.chat_view.visible = False
        self.meet_view.visible = False
        self.page.go("/inbox")

    def display_chat(self):
        print("Display chat")
        self.mail_view.visible = False
        self.chat_view.visible = True
        self.meet_view.visible = False
        self.page.go("/chat")

    def display_meet(self):
        print("Display meet")
        self.mail_view.visible = False
        self.chat_view.visible = False
        self.meet_view.visible = True
        self.page.go("/meet")
