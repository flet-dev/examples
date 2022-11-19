import flet as ft


def main(page: ft.Page):
    page.theme_mode = "light"

    def textbox_changed(e):
        t.value = e.control.value
        page.update()

    # ft.TextStyle object has 6 properties: size, weight, italic, font_family, color, bgcolor
    tb = ft.TextField(
        text_style=ft.TextStyle(size=15, italic=True, color=ft.colors.DEEP_ORANGE_600, bgcolor='limeaccent200'),

        label="Textbox with 'change' event and style:",
        label_style=ft.TextStyle(size=17, weight='bold', italic=True, color=ft.colors.BLUE, bgcolor=ft.colors.RED_700),

        hint_text="hint_text",
        hint_style=ft.TextStyle(size=15, weight='bold', italic=True, color=ft.colors.PINK_ACCENT, bgcolor="brown400"),

        helper_text="helper_text",
        helper_style=ft.TextStyle(size=14, weight='bold', color=ft.colors.DEEP_PURPLE, bgcolor=ft.colors.BLUE_50),

        counter_text="counter_text",
        counter_style=ft.TextStyle(size=14, italic=True, color=ft.colors.YELLOW, bgcolor=ft.colors.GREEN_500),

        on_change=textbox_changed,
    )

    t = ft.Text()

    page.add(tb, t)


ft.app(target=main)
