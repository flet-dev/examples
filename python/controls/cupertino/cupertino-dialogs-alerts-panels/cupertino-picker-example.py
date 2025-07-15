import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    selected_fruit_ref = ft.Ref[ft.Text]()
    fruits = [
        "Apple",
        "Mango",
        "Banana",
        "Orange",
        "Pineapple",
        "Strawberry",
    ]

    def handle_picker_change(e):
        selected_fruit_ref.current.value = fruits[int(e.data)]
        page.update()

    cupertino_picker = ft.CupertinoPicker(
        selected_index=3,
        magnification=1.22,
        squeeze=1.2,
        use_magnifier=True,
        on_change=handle_picker_change,
        controls=[ft.Text(value=f) for f in fruits],
    )

    page.add(
        ft.Row(
            tight=True,
            controls=[
                ft.Text("Selected Fruit:", size=23),
                ft.TextButton(
                    content=ft.Text(value=fruits[3], ref=selected_fruit_ref, size=23),
                    style=ft.ButtonStyle(color=ft.Colors.BLUE),
                    on_click=lambda e: page.show_dialog(
                        ft.CupertinoBottomSheet(
                            content=cupertino_picker,
                            height=216,
                            padding=ft.Padding.only(top=6),
                        )
                    ),
                ),
            ],
        ),
    )


ft.run(main)
