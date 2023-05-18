import flet as ft

name = "Customize Tabs theme"


def example():
    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Tab 1",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.icons.SEARCH),
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Tab 3",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
        ],
        expand=1,
    )

    c = ft.Container(
        content=t,
        height=300,
        width=300,
        border=ft.border.all(1, "black"),
        theme=ft.Theme(
            tabs_theme=ft.TabsTheme(
                divider_color=ft.colors.BLUE,
                indicator_color=ft.colors.RED,
                indicator_tab_size=True,
                label_color=ft.colors.GREEN,
                unselected_label_color=ft.colors.AMBER,
                overlay_color={
                    ft.MaterialState.FOCUSED: ft.colors.with_opacity(
                        0.2, ft.colors.GREEN
                    ),
                    ft.MaterialState.DEFAULT: ft.colors.with_opacity(
                        0.2, ft.colors.PINK
                    ),
                },
            )
        ),
    )

    return c
