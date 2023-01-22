from flet.buttons import RoundedRectangleBorder
from flet import (
    Page,
    Row,
    Text,
    TextButton,
    ButtonStyle,
    colors,
)


class LandingPage(Row):
    def __init__(
        self,
        app,
        page: Page,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.app = app
        self.page = page
        #self.app_layout = layout
        self.try_button = TextButton(
                                "Try it out", 
                                on_click=self.try_button_click,
                                style=ButtonStyle(
                                    bgcolor={
                                        "": colors.BLUE_300,
                                        "hovered": colors.BLUE_600
                                    },
                                    shape={
                                        "": RoundedRectangleBorder(radius=3)
                                    }
                                )
                            )
        self.signup_button = TextButton(
                                    "Create account",
                                    on_click=self.signup_button_click, 
                                    style=ButtonStyle(
                                        bgcolor={
                                            "": colors.BLUE_300,
                                            "hovered": colors.BLUE_600
                                        },
                                        shape={
                                            "": RoundedRectangleBorder(radius=3)
                                        }
                                    )
                                )
        self.controls = [self.try_button, self.signup_button]


    def try_button_click(self, i):
        #redirect to no auth live site.
        pass

    def signup_button_click(self, i):
        pass

    
