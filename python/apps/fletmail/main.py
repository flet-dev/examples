MOBILE_MAX_WIDTH = 640
import flet as ft
from components.mobile_view import MobileView
from components.web_view import WebView


def main(page: ft.Page):
    # page.width = 500 # Initial layout is "mobile"

    web_view = WebView()
    mobile_view = MobileView()

    def switch_view():
        # check if view needs to be changed:
        size = page.width
        if size > MOBILE_MAX_WIDTH:
            if isinstance(page.views[0], MobileView):
                print("Need to change to WebView")
                page.views.clear()
                page.views.append(web_view)
        else:
            if isinstance(page.views[0], WebView):
                print("Need to change to MobileView")
                page.views.clear()
                page.views.append(mobile_view)
        page.update()

    # Initial layout
    print(f"Initial page width: {[page.width]}")
    page.views.clear()
    page.views.append(web_view)
    switch_view()

    def page_resize(e):
        switch_view()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_resize = page_resize
    page.on_view_pop = view_pop  # triggered when clicking on "X" for New Message view

    def get_route_list(route):
        route_list = [item for item in route.split("/") if item != ""]
        return route_list

    def route_change(e):
        route_list = get_route_list(page.route)

        if len(route_list) == 0:
            page.go("/mail/inbox")
            print("Route len is 0")
        if len(route_list) == 1:
            print(route_list)
            if route_list[0] == ("mail"):
                page.views[0].display_mail("inbox")
            if route_list[0] == ("chat"):
                page.views[0].display_chat()
            elif route_list[0] == ("meet"):
                page.views[0].display_meet()
            else:
                print("Invalid route")
        if len(route_list) == 2:
            print(route_list)
            if route_list[0] == ("mail"):
                # if route_list[1] == ("inbox"):
                # page.views[0].display_inbox()
                page.views[0].display_mail(route_list[1])
            # elif route_list[0] == ("chat"):
            #     page.views[0].display_chat()
            # elif route_list[0] == ("meet"):
            #     page.views[0].display_meet()
            else:
                print("Invalid route")
        if len(route_list) == 3:
            print(route_list)
            if route_list[0] == ("mail"):
                page.views[0].mail_filter = route_list[1]
                # message = page.views[0].get_message(route_list[2])
                page.views[0].get_message(route_list[2])
                # page.views[0].display_message(message)
                page.views[0].display_message()
            else:
                print("Invalid route")

    page.on_route_change = route_change
    print(f"Initial route: {page.route}")
    page.go(page.route)


ft.app(main)
