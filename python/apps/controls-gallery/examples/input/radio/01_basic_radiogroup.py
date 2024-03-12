import flet as ft

name = "Basic RadioGroup"


def example():
    async def button_clicked(e):
        t.value = f"Your favorite color is:  {cg.value}"
        await t.update_async()

    t = ft.Text()
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    cg = ft.RadioGroup(
        content=ft.Column(
            [
                ft.Radio(value="red", label="Red"),
                ft.Radio(value="green", label="Green"),
                ft.Radio(value="blue", label="Blue"),
            ]
        )
    )

    return ft.Column([ft.Text("Select your favorite color:"), cg, b, t])
