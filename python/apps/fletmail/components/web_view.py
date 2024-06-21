from typing import List

import flet as ft
from components.app_view import AppView
from components.new_message_view import NewMessageWebView


class SecondaryMenuAction(ft.TextButton):
    def __init__(self, text, icon, on_click, data):
        super().__init__()
        self.content = ft.Row(
            controls=[
                ft.Icon(name=icon, color=ft.colors.BLACK),
                ft.Text(value=text, color=ft.colors.BLACK),
            ]
        )
        self.style = ft.ButtonStyle(padding=15)
        self.on_click = on_click
        self.data = data


class WebView(AppView):
    def __init__(self):
        super().__init__()
        self.logo = ft.Row(
            controls=[
                ft.Container(
                    padding=5, content=ft.Image(src=f"logo.svg"), width=50, height=50
                ),
                ft.Text(
                    "FletMail",
                    width=100,
                    style=ft.TextStyle(
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),
                ),
            ]
        )

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
            destinations=[
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
            ],
            on_change=self.nav_rail_changed,
        )

        self.compose_button = ft.FloatingActionButton(
            icon=ft.icons.CREATE, text="Compose", on_click=self.compose_clicked
        )
        self.new_chat_button = ft.FloatingActionButton(
            icon=ft.icons.CHAT, text="New Chat", on_click=self.new_chat_clicked
        )
        self.mail_actions = ft.Column(
            [
                SecondaryMenuAction(
                    text="Inbox",
                    icon=ft.icons.MAIL,
                    on_click=self.mail_filter_clicked,
                    data="inbox",
                ),
                SecondaryMenuAction(
                    text="Starred",
                    icon=ft.icons.STAR,
                    on_click=self.mail_filter_clicked,
                    data="starred",
                ),
                SecondaryMenuAction(
                    text="Spam",
                    icon=ft.icons.DELETE,
                    on_click=self.mail_filter_clicked,
                    data="spam",
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=0,
        )
        self.chat_actions = ft.Column(
            [
                SecondaryMenuAction(
                    text="Home",
                    icon=ft.icons.HOME,
                    on_click=self.chat_filter_clicked,
                    data="home",
                ),
                SecondaryMenuAction(
                    text="Starred",
                    icon=ft.icons.STAR,
                    on_click=self.chat_filter_clicked,
                    data="starred",
                ),
                SecondaryMenuAction(
                    text="Mentions",
                    icon=ft.icons.CHAT,
                    on_click=self.chat_filter_clicked,
                    data="mentions",
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=0,
        )

        self.mail_menu = ft.Column(
            [self.compose_button, self.mail_actions],
            width=150,
        )
        self.chat_menu = ft.Column(
            [self.new_chat_button, self.chat_actions],
            width=150,
        )

        self.messages_list = ft.ListView(controls=self.get_message_tiles(), expand=True)

        self.message_view = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            on_click=self.back_to_messages,
                        ),
                        ft.Text("Message title", style=ft.TextStyle(size=20)),
                    ]
                ),
                ft.Text(value="This is message body"),
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
                    content=ft.Column(
                        [ft.Text("Chat View", style=ft.TextStyle(size=20))]
                    ),
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
                    ft.Pagelet(
                        appbar=ft.AppBar(
                            leading=self.logo,
                            actions=[
                                ft.CircleAvatar(
                                    foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
                                    content=ft.Text("FF"),
                                ),
                            ],
                        ),
                        content=ft.Container(
                            content=ft.Column(
                                controls=[
                                    self.mail_view,
                                    self.chat_view,
                                    self.meet_view,
                                ],
                            ),
                            expand=True,
                        ),
                        expand=True,
                    ),
                ],
                expand=True,
            )
        ]

    def mail_filter_clicked(self, e):
        print(f"{e.control.data} clicked")
        self.selected_message = None
        self.mail_filter = e.control.data
        self.display_mail()

    def chat_filter_clicked(self, e):
        print(f"{e.control.data} clicked")
        for control in self.chat_actions.controls:
            control.style.bgcolor = ft.colors.SURFACE
        e.control.style.bgcolor = ft.colors.SECONDARY_CONTAINER
        # self.selected_message = None
        self.chat_filter = e.control.data
        self.display_chat()

    def nav_rail_changed(self, e):
        print(f"Selected action: {e.control.selected_index}")
        if e.control.selected_index == 0:
            self.display_mail()

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

    def new_chat_clicked(self, e):
        print("New chat clicked")

    def get_message_tiles(self):
        messages_list = []
        for message in self.messages:
            messages_list.append(
                ft.ListTile(
                    data=message,
                    leading=ft.Row(
                        width=150,
                        controls=[ft.Checkbox(), ft.Text(message.author, size=14)],
                    ),
                    title=ft.Text(
                        spans=[
                            ft.TextSpan(
                                text=message.title,
                                style=ft.TextStyle(weight=ft.FontWeight.W_600, size=14),
                            ),
                            ft.TextSpan(
                                text=f" - {message.body}",
                                style=ft.TextStyle(weight=ft.FontWeight.W_100, size=14),
                            ),
                        ],
                        max_lines=1,
                        overflow=ft.TextOverflow.ELLIPSIS,
                    ),
                    trailing=ft.Text(value=message.date),
                    on_click=self.message_clicked,
                )
            )
        return messages_list

    def message_clicked(self, e):
        print("Message clicked!")
        self.selected_message = e.control.data
        self.display_message()

    def display_message(self):
        print(f"Display message for {self.selected_message.id}")
        self.messages_list.visible = False
        self.message_view.visible = True
        self.message_view.controls[0].controls[
            1
        ].value = self.selected_message.title  # title of the message
        self.message_view.controls[1].value = (
            self.selected_message.body
        )  # Body of the message
        self.page.go(f"/mail/{self.mail_filter}/{self.selected_message.id}")

    def back_to_messages(self, e):
        print("Go back to messages!")
        self.selected_message = None
        self.display_mail()

    def display_mail(self):
        print("Display mail")
        for control in self.mail_actions.controls:
            if control.data != self.mail_filter:
                control.style.bgcolor = ft.colors.SURFACE
            else:
                control.style.bgcolor = ft.colors.SECONDARY_CONTAINER
        self.mail_view.visible = True
        self.chat_view.visible = False
        self.meet_view.visible = False
        if self.selected_message == None:
            self.messages_list.visible = True
            self.message_view.visible = False
            self.page.go(f"/mail/{self.mail_filter}")
        else:
            self.display_message()

    def display_chat(self):
        print("Display chat")
        for control in self.chat_actions.controls:
            if control.data != self.chat_filter:
                control.style.bgcolor = ft.colors.SURFACE
            else:
                control.style.bgcolor = ft.colors.SECONDARY_CONTAINER
        self.mail_view.visible = False
        self.chat_view.visible = True
        self.meet_view.visible = False
        self.page.go(f"/chat/{self.chat_filter}")

    def display_meet(self):
        print("Display meet")
        self.mail_view.visible = False
        self.chat_view.visible = False
        self.meet_view.visible = True
        self.page.go("/meet")
