import flet
from flet import Container, Page, ResponsiveRow, Text, TextField, colors


def main(page: Page):
    def page_resize(e):
        pw.value = f"{page.width} px"
        pw.update()

    page.on_resize = page_resize

    pw = Text(bottom=50, right=50, style="displaySmall")
    page.overlay.append(pw)
    page.add(
        ResponsiveRow(
            [
                Container(
                    Text("Column 1"),
                    padding=5,
                    bgcolor=colors.YELLOW,
                    col={"sm": 6, "md": 4, "xl": 2},
                ),
                Container(
                    Text("Column 2"),
                    padding=5,
                    bgcolor=colors.GREEN,
                    col={"sm": 6, "md": 4, "xl": 2},
                ),
                Container(
                    Text("Column 3"),
                    padding=5,
                    bgcolor=colors.BLUE,
                    col={"sm": 6, "md": 4, "xl": 2},
                ),
                Container(
                    Text("Column 4"),
                    padding=5,
                    bgcolor=colors.PINK_300,
                    col={"sm": 6, "md": 4, "xl": 2},
                ),
            ],
        ),
        ResponsiveRow(
            [
                TextField(label="TextField 1", col={"md": 4}),
                TextField(label="TextField 2", col={"md": 4}),
                TextField(label="TextField 3", col={"md": 4}),
            ],
            run_spacing={"xs": 10},
        ),
    )
    page_resize(None)


flet.app(target=main, port=8550, view=flet.FLET_APP)
