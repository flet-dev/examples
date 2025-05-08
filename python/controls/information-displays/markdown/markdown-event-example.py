import flet as ft


def main(page: ft.Page):
    def open_url(e):
        page.launch_url(e.data)

    page.add(
        ft.Markdown(
            "[inline-style](https://www.google.com)",
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            on_tap_link=open_url,
            expand=True,
        ),
    )


ft.run(main)
