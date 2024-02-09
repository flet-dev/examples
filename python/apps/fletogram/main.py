import logging

import flet as ft

from fletogram import Fletogram
from views.bottom_navigation_bar import BottomNavigationBar
from views.chats_view import ChatView

# logging.basicConfig(level=logging.DEBUG)


def main(page: ft.Page):

    # page.platform = ft.PagePlatform.ANDROID

    page.adaptive = True

    contacts_appbar = ft.AppBar(  # adaptive=True,
        leading=ft.TextButton("Edit"),
        title=ft.Text("Contacts"),
        actions=[
            ft.IconButton(icon=ft.icons.ADD_CARD),
        ],
    )
    settings_appbar = ft.AppBar(  # adaptive=True,
        # leading=ft.TextButton("Edit"),
        title=ft.Text("Settings"),
        # actions=[ft.IconButton(icon=ft.icons.ADD_CARD),]
    )

    def on_chat_clicked(chat):
        print(f"Display messages for {chat.name}")
        messages_view = ft.ListView(spacing=5)
        for message in chat.messages:
            if message.is_logged_user:
                alignment = ft.MainAxisAlignment.END
            else:
                alignment = ft.MainAxisAlignment.START
            messages_view.controls.append(
                ft.Row(
                    [message],
                    alignment=alignment,
                )
            )
            print(message.body)

        page.views.append(
            ft.View(
                "/chat",
                [
                    ft.AppBar(
                        title=ft.Text(chat.display_name),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    messages_view,
                ],
            )
        )

        page.update()

    fletogram = Fletogram(on_chat_clicked=on_chat_clicked)

    # def destination_changed(e):
    #     page.views.clear()
    #     page.views.append(tabs[e.control.selected_index])
    #     page.update()

    # bottom_navigation_bar = ft.NavigationBar(
    #     selected_index=1,
    #     destinations=[
    #         ft.NavigationDestination(
    #             icon=ft.icons.CONTACT_EMERGENCY,
    #             label="Contacts",
    #         ),
    #         ft.NavigationDestination(
    #             icon=ft.icons.CHAT,
    #             label="Chats",
    #         ),
    #         ft.NavigationDestination(
    #             icon=ft.icons.SETTINGS,
    #             label="Settings",
    #         ),
    #     ],
    #     on_change=destination_changed,
    # )

    chats_view = ChatView(fletogram=fletogram)
    contacts_view = ft.View(
        "/contacts",
        appbar=contacts_appbar,
        controls=[ft.ListView(spacing=5, controls=fletogram.users)],
        # navigation_bar=bottom_navigation_bar,
    )
    settings_view = ft.View(
        "/settings",
        appbar=settings_appbar,
        controls=[ft.Text("Settings")],
        # navigation_bar=bottom_navigation_bar,
    )

    tabs = [contacts_view, chats_view, settings_view]
    bottom_navigation_bar = BottomNavigationBar(tabs=tabs)

    page.window_width = 393
    page.window_height = 852

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_view_pop = view_pop
    page.views.clear()
    page.views.append(chats_view)
    page.update()


ft.app(target=main)
