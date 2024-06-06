MOBILE_MAX_WIDTH = 640
import flet as ft
from fletmail import FletMail
from secondary_menu import SecondaryMenuMobile, SecondaryMenuWeb
from web_layout import WebLayout


def main(page: ft.Page):

    # if page.window_width != None and page.window_width > 650:
    #     mobile_view = False
    # else:
    #     mobile_view = True

    # fletmail = FletMail()

    # nav_rail_destinations = []
    # nav_destinations = []

    # mail_secondary_menu_web = SecondaryMenuWeb()

    # def open_close_mobile_clicked(e):
    #     page.drawer.open = True
    #     page.drawer.update()

    # mobile_header = ft.Container(
    #     visible=False,
    #     content=ft.Row(
    #         [
    #             ft.IconButton(
    #                 icon=fletmail.open_close_menu.icon,
    #                 on_click=open_close_mobile_clicked,
    #             )
    #         ]
    #     ),
    # )

    # def create_navigation_destinations(fletmail):

    #     nav_rail_destinations.append(
    #         ft.NavigationRailDestination(
    #             icon=fletmail.open_close_menu.icon,
    #         )
    #     )

    #     for destination in fletmail.actions:
    #         nav_rail_destinations.append(
    #             ft.NavigationRailDestination(
    #                 label=destination.label, icon=destination.icon
    #             )
    #         )
    #         nav_destinations.append(ft.NavigationDestination(icon=destination.icon))

    # create_navigation_destinations(fletmail)

    # compose_button = ft.FloatingActionButton(icon=ft.icons.CREATE, text="Compose")

    # def do_action(e):
    #     print(f"Selected action: {e.control.selected_index}")
    #     if e.control.selected_index == 0:
    #         fletmail.open_close_menu.on_click()

    #         mail_secondary_menu_web.visible = not mail_secondary_menu_web.visible
    #         page.update()

    #     else:
    #         fletmail.actions[e.control.selected_index - 1].on_click()
    #         print(
    #             f"Need options for {fletmail.actions[e.control.selected_index-1].label}"
    #         )

    # rail = ft.NavigationRail(
    #     selected_index=0,
    #     label_type=ft.NavigationRailLabelType.ALL,
    #     bgcolor=ft.colors.PRIMARY_CONTAINER,
    #     # extended=True,
    #     min_width=100,
    #     min_extended_width=400,
    #     # leading=compose_button,
    #     group_alignment=-0.9,
    #     destinations=nav_rail_destinations,
    #     on_change=do_action,
    # )

    # bar = ft.NavigationBar(destinations=nav_destinations, on_change=do_action)
    # secondary_menu_drawer = SecondaryMenuMobile()

    web_layout = WebLayout()
    page.add(web_layout)

    # page.add(
    #     ft.Row(
    #         [
    #             rail,
    #             mail_secondary_menu_web,
    #             ft.Column(
    #                 [mobile_header, ft.Text("Body!")],
    #                 alignment=ft.MainAxisAlignment.START,
    #                 expand=True,
    #             ),
    #         ],
    #         expand=True,
    #     )
    # )

    # def display_mobile_layout():
    #     page.navigation_bar = bar
    #     page.floating_action_button = compose_button
    #     mail_secondary_menu_web.visible = False
    #     page.drawer = secondary_menu_drawer
    #     rail.visible = False
    #     mobile_header.visible = True
    #     page.update()

    # def display_web_layout():
    #     page.navigation_bar = None
    #     page.floating_action_button = None
    #     page.drawer = None
    #     rail.visible = True
    #     mobile_header.visible = False
    #     page.update()

    # if mobile_view:
    #     display_mobile_layout()
    # else:
    #     display_web_layout()

    # def page_resize(e):
    #     size = page.window_width
    #     print("New page size:", page.window_width, page.window_height)
    #     if (size != None) and (size > MOBILE_MAX_WIDTH):
    #         display_web_layout()
    #     else:
    #         display_mobile_layout()

    # page.on_resize = page_resize


ft.app(main)
