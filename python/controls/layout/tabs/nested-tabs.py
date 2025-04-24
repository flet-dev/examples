import flet as ft


def main(page: ft.Page):

    dt = ft.Tabs(
        is_secondary=True,
        tabs=[
            ft.Tab(text="Fast Food", content=ft.Text("Grab something on the go!")),
            ft.Tab(text="Fine Dining", content=ft.Text("Take your time!")),
        ],
    )
    et = ft.Tabs(
        is_secondary=True,
        tabs=[
            ft.Tab(text="Cinema", content=ft.Text("Find a Film!")),
            ft.Tab(text="Music", content=ft.Text("Listen to some Tunes!")),
        ],
    )
    lt = ft.Tabs(
        is_secondary=True,
        tabs=[
            ft.Tab(text="Hotel", content=ft.Text("Enjoy your Room!")),
            ft.Tab(text="Hostel", content=ft.Text("Grab a Bunk!")),
        ],
    )
    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Dining",
                icon=ft.Icons.RESTAURANT,
                content=dt,
            ),
            ft.Tab(
                text="Entertainment",
                icon=ft.Icons.LOCAL_ACTIVITY,
                content=et,
            ),
            ft.Tab(
                text="Lodging",
                icon=ft.Icons.HOTEL,
                content=lt,
            ),
        ],
        expand=1,
    )

    page.add(t)


ft.app(main)
