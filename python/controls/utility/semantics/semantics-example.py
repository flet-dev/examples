import flet as ft


def main(page: ft.Page):
    tf = ft.TextField(
        label="Occupation",
        hint_text="Use 20 words or less",
        value="What is your occupation?",
    )

    def on_focus(e):
        print("focus gained")

    def on_lose_focus(e):
        print("focus lost")

    page.add(
        ft.Column(
            [
                ft.Semantics(
                    tf,
                    label="Input your occupation",
                    on_did_gain_accessibility_focus=on_focus,
                    on_did_lose_accessibility_focus=on_lose_focus,
                ),
                ft.Icon(name="settings", color="#c1c1c1"),
            ]
        )
    )


ft.app(main)
