import flet as ft


def example():
    over_18 = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="yes", label="Yes"),
                ft.Radio(value="no", label="No"),
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

    return ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.TextField(label="First name"),
            ft.TextField(label="Last name"),
            ft.Divider(thickness=1),
            ft.Text("Are you over 18?"),
            over_18,
            ft.Divider(thickness=1),
            choice_of_instrument,
            ft.Text("Pick days for classes:"),
            monday,
            tuesday,
            wednesday,
            thursday,
            friday,
            saturday,
            sunday,
        ],
    )


def main(page: ft.Page):
    page.title = "Flet entry form example"
    page.window_width = 390
    page.window_height = 844
    page.add(example())


if __name__ == "__main__":
    ft.app(target=main)
