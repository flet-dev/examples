import flet as ft


def main(page):
    def button_clicked(e):
        t.value = f"Your favorite color is:  {cg.value}"
        page.update()

    t = ft.Text()
    b = ft.ElevatedButton(content="Submit", on_click=button_clicked)
    cg = ft.RadioGroup(
        content=ft.Column(
            [
                ft.CupertinoRadio(
                    value="red",
                    label="Red - Cupertino Radio",
                    active_color=ft.Colors.RED,
                    inactive_color=ft.Colors.RED,
                ),
                ft.Radio(
                    value="green",
                    label="Green - Material Radio",
                    fill_color=ft.Colors.GREEN,
                ),
                ft.Radio(
                    value="blue",
                    label="Blue - Adaptive Radio",
                    adaptive=True,
                    active_color=ft.Colors.BLUE,
                ),
            ]
        )
    )

    page.add(ft.Text("Select your favorite color:"), cg, b, t)


ft.run(main)
