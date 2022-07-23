import flet
from flet import Page, Text


def main(page: Page):
    page.add(Text(f"Initial route: {page.route}"))

    def route_change(route):
        page.add(Text(f"New route: {route}"))

    page.on_route_change = route_change
    page.update()


flet.app(target=main, view=flet.WEB_BROWSER)
