import flet as ft


def main(page):

    def close_anchor(e):
        text = f"Color {e.control.data}"
        print(f"closing view from {text}")
        anchor.close_view(text)
        ob.focus()

    def handle_change(e):
        print(f"handle_change e.data: {e.data}")

    def handle_submit(e):
        print(f"handle_submit e.data: {e.data}")
        page.add(ft.Text(f"Search submitted for: {e.data}"))
        page.update()

    def handle_tap(e):
        print(f"handle_tap")
        anchor.open_view()

    def toggle_open_view(e):
        if ob.content == "Open Search View":
            ob.content = "Close Search View"
            anchor.open_view()
        else:
            ob.content = "Open Search View"
            anchor.close_view(e.data)
        page.update()

    def handle_tap_outside_bar(e):
        print("handle_tap_outside_bar")
        if ob.content == "Open Search View":
            ob.content = "Close Search View"
            anchor.open_view()
        else:
            ob.content = "Open Search View"
            anchor.close_view(e.data)
        page.update()

    anchor = ft.SearchBar(
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
    )
    ob = ft.OutlinedButton(content="Open Search View", on_click=toggle_open_view)

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[ob],
        ),
        anchor,
    )


ft.run(main)
