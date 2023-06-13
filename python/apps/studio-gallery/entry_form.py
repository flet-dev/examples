import flet as ft


def example():
    gender = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="female", label="Female"),
                ft.Radio(value="male", label="Male"),
                ft.Radio(value="not_specified", label="Not specified"),
            ]
        )
    )

    choice_of_instrument = ft.Dropdown(
        label="Choice of instrument",
        options=[
            ft.dropdown.Option("Piano"),
            ft.dropdown.Option("Violin"),
            ft.dropdown.Option("Guitar"),
        ],
    )

    monday = ft.Checkbox(label="Monday", value=False)
    tuesday = ft.Checkbox(label="Tuesday", value=False)
    wednesday = ft.Checkbox(label="Wednesday", value=False)
    thursday = ft.Checkbox(label="Thursday", value=False)
    friday = ft.Checkbox(label="Friday", value=False)
    saturday = ft.Checkbox(label="Saturday", value=False)
    sunday = ft.Checkbox(label="Sunday", value=False)

    def submit_form(e):
        print("Submit form")

    submit = ft.FilledButton("Submit", on_click=submit_form)

    return ft.Column(
        expand=True,
        # alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.TextField(label="First name", keyboard_type=ft.KeyboardType.NAME),
            ft.TextField(label="Last name", keyboard_type=ft.KeyboardType.NAME),
            ft.TextField(label="Email", keyboard_type=ft.KeyboardType.EMAIL),
            ft.TextField(label="Age", keyboard_type=ft.KeyboardType.NUMBER),
            ft.Text("Gender:"),
            gender,
            ft.Divider(thickness=1),
            choice_of_instrument,
            ft.Text("Pick days for classes:"),
            monday,
            tuesday,
            wednesday,
            thursday,
            friday,
            ft.Row(controls=[submit], alignment=ft.MainAxisAlignment.CENTER),
        ],
    )


def main(page: ft.Page):
    page.title = "Flet entry form example"
    page.window_width = 390
    page.window_height = 844
    page.add(example())


if __name__ == "__main__":
    ft.app(target=main)
