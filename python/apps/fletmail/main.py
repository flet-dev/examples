MOBILE_MAX_WIDTH = 640
import flet as ft
from mobile_layout import MobileLayout
from web_layout import WebLayout


def main(page: ft.Page):

    # compose_button = ft.FloatingActionButton(icon=ft.icons.CREATE, text="Compose")

    web_layout = WebLayout()
    mobile_layout = MobileLayout()
    page.add(web_layout)

    def page_resize(e):
        size = page.window_width
        print("New page size:", page.window_width, page.window_height)
        if (size != None) and (size > MOBILE_MAX_WIDTH):
            page.controls = [WebLayout()]
            print("Showing web layout")
        else:
            page.controls = [MobileLayout()]
            print("Showing mobile layout")
        page.update()

    page.on_resize = page_resize


ft.app(main)
