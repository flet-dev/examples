import os

import flet
from flet import ElevatedButton, Page
from flet.auth.providers.github_oauth_provider import GitHubOAuthProvider


def main(page: Page):

    provider = GitHubOAuthProvider(
        client_id=os.getenv("GITHUB_CLIENT_ID"),
        client_secret=os.getenv("GITHUB_CLIENT_SECRET"),
        redirect_url="http://localhost:8550/api/oauth/redirect",
    )

    def login_click(e):
        page.login(provider)

    def on_login(e):
        print("Access token:", page.auth.token.access_token)
        print("User ID:", page.auth.user.id)

    page.on_login = on_login
    page.add(ElevatedButton("Login with GitHub", on_click=login_click))


flet.app(target=main, port=8550, view=flet.WEB_BROWSER)
