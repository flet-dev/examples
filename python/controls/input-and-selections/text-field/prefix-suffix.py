import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{pr.value}', '{sf.value}', '{ps.value}', '{icon.value}'."
        page.update()

    t = ft.Text()
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    pr = ft.TextField(label="With prefix", prefix_text="https://")
    sf = ft.TextField(label="With suffix", suffix_text=".com")
    ps = ft.TextField(
        label="With prefix and suffix", prefix_text="https://", suffix_text=".com"
    )
    icon = ft.TextField(
        label="My favorite color",
        icon=ft.Icons.FORMAT_SIZE,
        hint_text="Type your favorite color",
        helper_text="You can type only one color",
        counter_text="0 symbols typed",
        prefix_icon=ft.Icons.COLOR_LENS,
        suffix_text="...is your color",
    )
    page.add(pr, sf, ps, icon, b, t)


ft.app(main)
