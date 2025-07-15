import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    def textbox_changed(e):
        message.value = e.control.value
        page.update()

    page.add(
        ft.TextField(
            text_style=ft.TextStyle(
                size=15,
                italic=True,
                color=ft.Colors.DEEP_ORANGE_600,
                bgcolor="limeaccent200",
            ),
            label="Textbox with 'change' event and style:",
            label_style=ft.TextStyle(
                size=17,
                weight=ft.FontWeight.BOLD,
                italic=True,
                color=ft.Colors.BLUE,
                bgcolor=ft.Colors.RED_700,
            ),
            hint_text="hint",
            hint_style=ft.TextStyle(
                size=15,
                weight=ft.FontWeight.BOLD,
                italic=True,
                color=ft.Colors.PINK_ACCENT,
                bgcolor="brown400",
            ),
            helper="helper",
            helper_style=ft.TextStyle(
                size=14,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.DEEP_PURPLE,
                bgcolor=ft.Colors.BLUE_50,
            ),
            counter="counter",
            counter_style=ft.TextStyle(
                size=14,
                italic=True,
                color=ft.Colors.YELLOW,
                bgcolor=ft.Colors.GREEN_500,
            ),
            on_change=textbox_changed,
        ),
        message := ft.Text(),
    )


ft.run(main)
