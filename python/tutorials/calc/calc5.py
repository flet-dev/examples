import flet as ft


class CalcButton(ft.ElevatedButton):
    def __init__(self, text, expand=1):
        super().__init__()
        self.reset()
        self.text = text
        self.expand = expand
        self.on_click = self.button_clicked

    def button_clicked(self, e):
        print(e.control)
        data = e.control.text
        self.result = self.page.calc.result
        if self.page.calc.result.value == "Error" or data == "AC":
            self.page.calc.result.value = "0"
            self.reset()

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.page.calc.result.value == "0" or self.new_operand == True:
                self.page.calc.result.value = data
                self.new_operand = False
            else:
                self.page.calc.result.value = self.page.calc.result.value + data

        elif data in ("+", "-", "*", "/"):
            self.page.calc.result.value = self.calculate(
                self.operand1, float(self.page.calc.result.value), self.operator
            )
            self.operator = data
            if self.page.calc.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.page.calc.result.value)
            self.new_operand = True

        elif data in ("="):
            self.page.calc.result.value = self.calculate(
                self.operand1, float(self.page.calc.result.value), self.operator
            )
            self.reset()

        elif data in ("%"):
            self.page.calc.result.value = float(self.page.calc.result.value) / 100
            self.reset()

        elif data in ("+/-"):
            if float(self.page.calc.result.value) > 0:
                self.page.calc.result.value = "-" + str(self.page.calc.result.value)

            elif float(self.page.calc.result.value) < 0:
                self.page.calc.result.value = str(
                    self.format_number(abs(float(self.page.calc.result.value)))
                )

        self.update()

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):

        if operator == "+":
            return self.format_number(operand1 + operand2)

        elif operator == "-":
            return self.format_number(operand1 - operand2)

        elif operator == "*":
            return self.format_number(operand1 * operand2)

        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True


class DigitButton(CalcButton):
    def __init__(self, text, expand=1):
        CalcButton.__init__(self, text, expand)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE


class ActionButton(CalcButton):
    def __init__(self, text):
        CalcButton.__init__(self, text)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE


class ExtraActionButton(CalcButton):
    def __init__(self, text):
        CalcButton.__init__(self, text)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK


class CalculatorApp(ft.Container):
    # application's root control (i.e. "view") containing all other controls
    def __init__(self):
        super().__init__()

        self.result = ft.Text(value="0", color=ft.colors.WHITE, size=20)
        self.width = 350
        self.bgcolor = ft.colors.BLACK
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20
        self.content = ft.Column(
            controls=[
                ft.Row(controls=[self.result], alignment="end"),
                ft.Row(
                    controls=[
                        ExtraActionButton(text="AC"),
                        ExtraActionButton(text="+/-"),
                        ExtraActionButton(text="%"),
                        ActionButton(text="/"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="7"),
                        DigitButton(text="8"),
                        DigitButton(text="9"),
                        ActionButton(text="*"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="4"),
                        DigitButton(text="5"),
                        DigitButton(text="6"),
                        ActionButton(text="-"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="1"),
                        DigitButton(text="2"),
                        DigitButton(text="3"),
                        ActionButton(text="+"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="0", expand=2),
                        DigitButton(text="."),
                        ActionButton(text="="),
                    ]
                ),
            ]
        )


def main(page: ft.Page):
    page.title = "Calc App"
    # create application instance
    page.calc = CalculatorApp()

    # add application's root control to the page
    page.add(page.calc)


ft.app(target=main)
