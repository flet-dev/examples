import flet as ft


def main(page: ft.Page):
    def handle_link_tap(e):
        page.launch_url(e.data)

    page.add(
        ft.Markdown(
            value="[inline-style](https://www.google.com)",
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            on_tap_link=handle_link_tap,
            expand=True,
        ),
    )


ft.run(main)
