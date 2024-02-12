import logging

import flet as ft

from data.fletogram import Fletogram
from views.chats_view import ChatView

# logging.basicConfig(level=logging.DEBUG)


def main(page: ft.Page):

    # page.platform = ft.PagePlatform.ANDROID

    page.adaptive = True

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

    fletogram = Fletogram(page=page, on_chat_clicked=on_chat_clicked)

    page.window_width = 393
    page.window_height = 852

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_view_pop = view_pop
    page.views.clear()
    page.views.append(fletogram.tabs[1])
    page.update()


ft.app(target=main)
