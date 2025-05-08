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
                ft.Radio(value="red", label="Red"),
                ft.Radio(value="green", label="Green"),
                ft.Radio(value="blue", label="Blue"),
            ]
        )
    )

    page.add(ft.Text("Select your favorite color:"), cg, b, t)


ft.run(main)
