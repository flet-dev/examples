import logging
import flet as ft
from fletogram import Fletogram

logging.basicConfig(level=logging.DEBUG)


def main(page: ft.Page):

    chats_appbar = ft.AppBar(adaptive=True, 
                            leading=ft.TextButton("Edit"), 
                            title=ft.Text("Chats"), 
                            actions=[ft.IconButton(icon=ft.icons.ADD_COMMENT),])
    contacts_appbar = ft.AppBar(adaptive=True, 
                                leading=ft.TextButton("Edit"), 
                                title=ft.Text("Contacts"), 
                                actions=[ft.IconButton(icon=ft.icons.ADD_CARD),])
    def destination_changed(e):
        if e.control.selected_index==0:
            contacts_view.visible = True
            chats_view.visible = False
            messages_view.visible = False
            e.control.page.appbar = contacts_appbar
        if e.control.selected_index==1:
            contacts_view.visible = False
            messages_view.visible = False
            chats_view.visible = True
            e.control.page.appbar = chats_appbar
        page.update()
    
    def on_chat_clicked(chat):
        print(f"Display messages for {chat.name}")
        #contacts_view.visible = False
        #chats_view.visible = False
        #messages_view.visible = True
        messages_view.controls = []
        for message in chat.messages:
            messages_view.controls.append(ft.Text(message.body))
            print(message.body)
        
        page.views.append(
            ft.View(
                "/chat",
                [
                    ft.AppBar(title=ft.Text("Messages"), bgcolor=ft.colors.SURFACE_VARIANT),
                    #ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                    messages_view
                ],
            )
        )

        page.update()

    bottom_navigation_bar = ft.NavigationBar(selected_index=1, destinations=[
            ft.NavigationDestination(icon=ft.icons.CONTACT_EMERGENCY, label="Contacts",),
            ft.NavigationDestination(icon=ft.icons.CHAT, label="Chats",),
            ft.NavigationDestination(
                icon=ft.icons.SETTINGS,
                label="Settings",
            ),
        ],
        on_change=destination_changed)

    page.appbar = chats_appbar
    page.navigation_bar = bottom_navigation_bar
    page.window_width = 393
    page.window_height = 852
    fletogram = Fletogram(on_chat_clicked=on_chat_clicked)

    chats_view = ft.ListView(controls=fletogram.chats)
    contacts_view = ft.ListView(controls=fletogram.users, visible=False)
    messages_view = ft.Column(controls=[])

    page.add(
        chats_view,
        contacts_view,
        messages_view
    )
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_view_pop = view_pop

ft.app(target=main)