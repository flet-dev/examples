import flet as ft


def main(page: ft.Page):
    def close_anchor(e: ft.Event[ft.ListTile]):
        anchor.close_view(f"Color {e.control.data}")
        button.focus()

    def handle_change(e: ft.Event[ft.SearchBar]):
        print(f"handle_change e.data: {e.data}")

    def handle_submit(e: ft.Event[ft.SearchBar]):
        print(f"handle_submit e.data: {e.data}")
        page.add(ft.Text(f"Search submitted for: {e.data}"))
        page.update()

    def handle_tap(e: ft.Event[ft.SearchBar]):
        print("handle_tap")
        anchor.open_view()

    def toggle_open_view(e: ft.Event[ft.OutlinedButton]):
        if button.content == "Open Search View":
            button.content = "Close Search View"
            anchor.open_view()
        else:
            button.content = "Open Search View"
            anchor.close_view(e.data)
        page.update()

    def handle_tap_outside_bar(e: ft.Event[ft.SearchBar]):
        print("handle_tap_outside_bar")
        if button.content == "Open Search View":
            button.content = "Close Search View"
            anchor.open_view()
        else:
            button.content = "Open Search View"
            anchor.close_view(e.data)
        page.update()

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                button := ft.OutlinedButton(
                    content="Open Search View", on_click=toggle_open_view
                )
            ],
        ),
        anchor := ft.SearchBar(
            view_elevation=4,
            divider_color=ft.Colors.AMBER,
            bar_hint_text="Search colors...",
            view_hint_text="Choose a color from the suggestions...",
            on_change=handle_change,
            on_submit=handle_submit,
            on_tap=handle_tap,
            # on_tap_outside_bar=handle_tap_outside_bar,
            controls=[
                ft.ListTile(title=ft.Text(f"Color {i}"), on_click=close_anchor, data=i)
                for i in range(10)
            ],
        ),
    )


ft.run(main)
