import logging

import flet as ft

from data.fletogram import Fletogram

# logging.basicConfig(level=logging.DEBUG)


def main(page: ft.Page):

    # page.platform = ft.PagePlatform.ANDROID

    # page.adaptive = True

    fletogram = Fletogram(page=page)


ft.app(target=main)
