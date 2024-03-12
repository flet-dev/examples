import flet as ft

name = "CupertinoRadio example"


def example():
    async def button_clicked(e):
        t.value = f"Your favorite color is:  {cg.value}"
        await t.update_async()

    t = ft.Text()
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    cg = ft.RadioGroup(
        content=ft.Column(
            [
                ft.CupertinoRadio(
                    value="red",
                    label="Red - Cupertino Radio",
                    active_color=ft.colors.RED,
                    inactive_color=ft.colors.RED,
                ),
                ft.Radio(
                    value="green",
                    label="Green - Material Radio",
                    fill_color=ft.colors.GREEN,
                ),
                ft.Tooltip(
                    message="Adaptive Radio shows as CupertinoRadio on macOS and iOS and as Radio on other platforms",
                    content=ft.Radio(
                        value="blue",
                        label="Blue - Adaptive Radio",
                        adaptive=True,
                        active_color=ft.colors.BLUE,
                    ),
                ),
            ]
        )
    )

    return ft.Column([ft.Text("Select your favorite color:"), cg, b, t])
