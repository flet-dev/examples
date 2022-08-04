import flet
from flet import Text

from layout import first_name, greetings, last_name, init_layout


class Page():
    def __init__(self, page):
        self.page = page
        init_layout(self.page, logic={'btn_click': self.btn_click})

    def btn_click(self, e):
        greetings.current.controls.append(
            Text(f"Hello, {first_name.current.value} {last_name.current.value}!")
        )
        first_name.current.value = ""
        last_name.current.value = ""
        self.page.update()
        first_name.current.focus()


flet.app(target=Page)
