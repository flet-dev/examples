import json
import os

import flet
import requests
from flet import (
    AppBar,
    ElevatedButton,
    Icon,
    ListTile,
    ListView,
    LoginEvent,
    Page,
    Row,
    Text,
    icons,
)
from flet.auth.providers.github_oauth_provider import GitHubOAuthProvider
from flet.security import decrypt, encrypt


def main(page: Page):
    # encryption passphrase
    secret_key = os.getenv("MY_APP_SECRET_KEY")

    # configure provider
    provider = GitHubOAuthProvider(
        client_id=os.getenv("GITHUB_CLIENT_ID"),
        client_secret=os.getenv("GITHUB_CLIENT_SECRET"),
        redirect_url="http://localhost:8550/api/oauth/redirect",
    )

    # client storage keys
    AUTH_TOKEN_KEY = "myapp.auth_token"

    def perform_login(e):
        # perform login
        saved_token = None
        ejt = page.client_storage.get(AUTH_TOKEN_KEY)
        if ejt:
            saved_token = decrypt(ejt, secret_key)
        if e is not None or saved_token is not None:
            page.login(provider, saved_token=saved_token, scope=["public_repo"])

    def on_login(e: LoginEvent):
        if e.error:
            raise Exception(e.error)

        # save token in a client storage
        jt = page.auth.token.to_json()
        ejt = encrypt(jt, secret_key)
        page.client_storage.set(AUTH_TOKEN_KEY, ejt)

        logged_user.value = f"Hello, {page.auth.user['name']}!"
        toggle_login_buttons()
        list_github_repositories()
        page.update()

    def list_github_repositories():
        repos_view.controls.clear()
        if page.auth:
            headers = {
                "Authorization": "Bearer {}".format(page.auth.token.access_token)
            }
            repos_resp = requests.get(
                "https://api.github.com/user/repos", headers=headers
            )
            user_repos = json.loads(repos_resp.text)
            for repo in user_repos:
                repos_view.controls.append(
                    ListTile(
                        leading=Icon(icons.FOLDER_ROUNDED),
                        title=Text(repo["full_name"]),
                    )
                )

    def logout_button_click(e):
        page.client_storage.remove(AUTH_TOKEN_KEY)
        page.logout()

    def on_logout(e):
        toggle_login_buttons()
        list_github_repositories()
        page.update()

    def toggle_login_buttons():
        login_button.visible = page.auth is None
        logged_user.visible = logout_button.visible = page.auth is not None

    logged_user = Text()
    login_button = ElevatedButton("Login with GitHub", on_click=perform_login)
    logout_button = ElevatedButton("Logout", on_click=logout_button_click)
    repos_view = ListView(expand=True)
    page.on_login = on_login
    page.on_logout = on_logout
    toggle_login_buttons()
    perform_login(None)
    page.add(Row([logged_user, login_button, logout_button]), repos_view)


flet.app(target=main, port=8550, view=flet.WEB_BROWSER)
