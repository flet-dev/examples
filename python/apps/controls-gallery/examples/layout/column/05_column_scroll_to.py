import flet as ft

name = "Controlling scroll position for Column"


def example():
    cl = ft.Column(
        spacing=10,
        height=180,
        width=300,
        scroll=ft.ScrollMode.ALWAYS,
        controls=[
            ft.Container(
                ft.Text("Section A"),
                alignment=ft.alignment.top_left,
                bgcolor=ft.colors.YELLOW_200,
                height=100,
                key="A",
            ),
            ft.Container(
                ft.Text("Section B"),
                alignment=ft.alignment.top_left,
                bgcolor=ft.colors.GREEN_200,
                height=100,
                key="B",
            ),
            ft.Container(
                ft.Text("Section C"),
                alignment=ft.alignment.top_left,
                bgcolor=ft.colors.BLUE_200,
                height=100,
                key="C",
            ),
            ft.Container(
                ft.Text("Section D"),
                alignment=ft.alignment.top_left,
                bgcolor=ft.colors.PINK_200,
                height=100,
                key="D",
            ),
        ],
    )

    async def scroll_to_a(_):
        await cl.scroll_to_async(key="A", duration=1000)

    async def scroll_to_b(_):
        await cl.scroll_to_async(key="B", duration=1000)

    async def scroll_to_c(_):
        await cl.scroll_to_async(key="C", duration=1000)

    async def scroll_to_d(_):
        await cl.scroll_to_async(key="D", duration=1000)

    return ft.Column(
        [
            ft.Container(cl, border=ft.border.all(1)),
            ft.Column(
                [
                    ft.Text("Scroll to:"),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "Section A",
                                on_click=scroll_to_a,
                            ),
                            ft.ElevatedButton(
                                "Section B",
                                on_click=scroll_to_b,
                            ),
                            ft.ElevatedButton(
                                "Section C",
                                on_click=scroll_to_c,
                            ),
                            ft.ElevatedButton(
                                "Section D",
                                on_click=scroll_to_d,
                            ),
                        ]
                    ),
                ]
            ),
        ]
    )
