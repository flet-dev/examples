MOBILE_MAX_WIDTH = 640
import flet as ft
from mobile_view import MobileView
from web_view import WebView


def main(page: ft.Page):
    # page.window_width = 500

    # compose_button = ft.FloatingActionButton(icon=ft.icons.CREATE, text="Compose")

    web_view = WebView()
    mobile_view = MobileView()

    def get_page_design():
        size = page.window_width
        print("Page size:", page.window_width, page.window_height)
        if (size != None) and (size > MOBILE_MAX_WIDTH):
            return "web"
        else:
            return "mobile"

    def switch_view():
        # the last view in the list will be shown on the page
        temp = page.views[1]
        page.views[1] = page.views[2]
        page.views[2] = temp
        page.update()

    page.design = get_page_design()

    page.views.append(mobile_view)
    page.views.append(web_view)
    if page.design == "mobile":
        switch_view()

    page.update()

    def page_resize(e):
        new_design = get_page_design()
        if page.design != new_design:
            switch_view()
            page.design = new_design

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_resize = page_resize
    page.on_view_pop = view_pop


ft.app(main)
