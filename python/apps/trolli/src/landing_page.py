import os
from flet.buttons import RoundedRectangleBorder
from flet.auth.providers.auth0_oauth_provider import Auth0OAuthProvider
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
            ),
            width=200
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
            ),
            width=200
        )
        self.controls = [self.try_button, self.signup_button]

    def try_button_click(self, e):
        # redirect to no auth live site.
        pass

    def signup_button_click(self, e):
        print("signup button clicked")
        provider = Auth0OAuthProvider(
            domain="dev-j3wnirdjarxj51uz.us.auth0.com",
            client_id=os.getenv("AUTH0_CLIENT_ID"),
            client_secret=os.getenv("AUTH0_CLIENT_SECRET"),
            redirect_url="http://localhost:8088/api/oauth/redirect",
            query_params="?screen_hint=signup"
        )
        # self.app.provider.domain
        self.page.login(provider)
