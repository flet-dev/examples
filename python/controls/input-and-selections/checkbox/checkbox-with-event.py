import flet as ft


def main(page: ft.Page):
    def checkbox_changed(e):
        page.add(ft.Text(f"Checkbox value changed to {c.value}"))
        page.update()

    c = ft.Checkbox(label="Checkbox with 'change' event", on_change=checkbox_changed)

    page.add(c)


ft.run(main)
