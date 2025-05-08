import logging
from time import sleep

import flet as ft


def main(page: ft.Page):
    page.title = "Tabs example"

    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                label="Tab 1",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.Alignment.center()
                ),
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.Icons.MESSAGE),
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                label="Tab 3",
                icon=ft.Icons.IRON,
                content=ft.Text("This is Tab 3"),
            ),
        ],
        expand=1,
    )

    page.add(t)

    sleep(7)
    t.selected_index = 2
    page.update()
    sleep(3)
    t.selected_index = 0
    page.update()
    sleep(3)
    t.selected_index = 1
    t.tabs.pop(0)
    t.tabs[1].content = ft.Text("Blah blah blah")
    page.update()
    sleep(3)
    t.tabs.clear()
    page.update()
    sleep(3)
    t.tabs.append(
        ft.Tab(
            label="Tab 4",
            icon=ft.Icons.LOCK,
            content=ft.Text("This is Tab 4"),
        )
    )
    t.tabs.append(
        ft.Tab(
            label="Tab 5",
            icon=ft.Icons.SIP_SHARP,
            content=ft.Text("This is Tab 5"),
        )
    )
    page.update()


ft.run(main)
