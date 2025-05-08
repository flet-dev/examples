import flet as ft


def main(page: ft.Page):
    cl = ft.Column(
        spacing=10,
        height=180,
        width=300,
        scroll=ft.ScrollMode.ALWAYS,
        controls=[
            ft.Container(
                ft.Text("Section A"),
                alignment=ft.alignment.top_left,
                bgcolor=ft.Colors.YELLOW_200,
                height=100,
                scroll_key="A",
            ),
            ft.Container(
                ft.Text("Section B"),
                alignment=ft.alignment.top_left,
                bgcolor=ft.Colors.GREEN_200,
                height=100,
                scroll_key="B",
            ),
            ft.Container(
                ft.Text("Section C"),
                alignment=ft.alignment.top_left,
                bgcolor=ft.Colors.BLUE_200,
                height=100,
                scroll_key="C",
            ),
            ft.Container(
                ft.Text("Section D"),
                alignment=ft.alignment.top_left,
                bgcolor=ft.Colors.PINK_200,
                height=100,
                scroll_key="D",
            ),
        ],
    )

    page.add(
        ft.Container(cl, border=ft.border.all(1)),
        ft.Column(
            [
                ft.Text("Scroll to:"),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Section A",
                            on_click=lambda _: cl.scroll_to(
                                scroll_key="A", duration=1000
                            ),
                        ),
                        ft.ElevatedButton(
                            "Section B",
                            on_click=lambda _: cl.scroll_to(
                                scroll_key="B", duration=1000
                            ),
                        ),
                        ft.ElevatedButton(
                            "Section C",
                            on_click=lambda _: cl.scroll_to(
                                scroll_key="C", duration=1000
                            ),
                        ),
                        ft.ElevatedButton(
                            "Section D",
                            on_click=lambda _: cl.scroll_to(
                                scroll_key="D", duration=1000
                            ),
                        ),
                    ]
                ),
            ]
        ),
    )


ft.run(main)
