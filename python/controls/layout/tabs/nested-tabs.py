import flet as ft


def main(page: ft.Page):

    dt = ft.Tabs(
        is_secondary=True,
        tabs=[
            ft.Tab(label="Fast Food", content=ft.Text("Grab something on the go!")),
            ft.Tab(label="Fine Dining", content=ft.Text("Take your time!")),
        ],
    )
    et = ft.Tabs(
        is_secondary=True,
        tabs=[
            ft.Tab(label="Cinema", content=ft.Text("Find a Film!")),
            ft.Tab(label="Music", content=ft.Text("Listen to some Tunes!")),
        ],
    )
    lt = ft.Tabs(
        is_secondary=True,
        tabs=[
            ft.Tab(label="Hotel", content=ft.Text("Enjoy your Room!")),
            ft.Tab(label="Hostel", content=ft.Text("Grab a Bunk!")),
        ],
    )
    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                label="Dining",
                icon=ft.Icons.RESTAURANT,
                content=dt,
            ),
            ft.Tab(
                label="Entertainment",
                icon=ft.Icons.LOCAL_ACTIVITY,
                content=et,
            ),
            ft.Tab(
                label="Lodging",
                icon=ft.Icons.HOTEL,
                content=lt,
            ),
        ],
        expand=1,
    )

    page.add(t)


ft.app(main)
