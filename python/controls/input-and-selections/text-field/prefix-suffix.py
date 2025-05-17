import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{pr.value}', '{sf.value}', '{ps.value}', '{icon.value}'."
        page.update()

    t = ft.Text()
    b = ft.ElevatedButton(content="Submit", on_click=button_clicked)
    pr = ft.TextField(label="With prefix", prefix="https://")
    sf = ft.TextField(label="With suffix", suffix=".com")
    ps = ft.TextField(
        label="With prefix and suffix",
        prefix="https://",
        suffix=".com",
        enable_interactive_selection=True,
    )
    icon = ft.TextField(
        label="My favorite color",
        icon=ft.Icons.FORMAT_SIZE,
        hint_text="Type your favorite color",
        helper="You can type only one color",
        counter="{value_length}/{max_length} chars used",
        prefix_icon=ft.Icons.COLOR_LENS,
        suffix="...is your color",
        max_length=20,
    )
    page.add(pr, sf, ps, icon, b, t)


ft.run(main)
