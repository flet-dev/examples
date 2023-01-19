import logging
import os
from itertools import islice

import flet
from flet import (
    Column,
    Container,
    GridView,
    Icon,
    IconButton,
    Page,
    Row,
    SnackBar,
    Text,
    TextButton,
    TextField,
    UserControl,
    alignment,
    colors,
    icons,
)

# logging.basicConfig(level=logging.INFO)

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


class IconBrowser(UserControl):
    def __init__(self, expand=False, height=500):
        super().__init__()
        if expand:
            self.expand = expand
        else:
            self.height = height

    def build(self):
        def batches(iterable, batch_size):
            iterator = iter(iterable)
            while batch := list(islice(iterator, batch_size)):
                yield batch

        # fetch all icon constants from icons.py module
        icons_list = []
        list_started = False
        for key, value in vars(icons).items():
            if key == "TEN_K":
                list_started = True
            if list_started:
                icons_list.append(value)

        search_txt = TextField(
            expand=1,
            hint_text="Enter keyword and press search button",
            autofocus=True,
            on_submit=lambda e: display_icons(e.control.value),
        )

        def search_click(e):
            display_icons(search_txt.value)

        search_query = Row(
            [search_txt, IconButton(icon=icons.SEARCH, on_click=search_click)]
        )

        search_results = GridView(
            expand=1,
            runs_count=10,
            max_extent=150,
            spacing=5,
            run_spacing=5,
            child_aspect_ratio=1,
        )
        status_bar = Text()

        def copy_to_clipboard(e):
            icon_key = e.control.data
            print("Copy to clipboard:", icon_key)
            self.page.set_clipboard(e.control.data)
            self.page.show_snack_bar(SnackBar(Text(f"Copied {icon_key}"), open=True))

        def search_icons(search_term: str):
            for icon_name in icons_list:
                if search_term != "" and search_term in icon_name:
                    yield icon_name

        def display_icons(search_term: str):

            # clean search results
            search_query.disabled = True
            self.update()

            search_results.clean()

            for batch in batches(search_icons(search_term.lower()), 200):
                for icon_name in batch:
                    icon_key = f"icons.{icon_name.upper()}"
                    search_results.controls.append(
                        TextButton(
                            content=Container(
                                content=Column(
                                    [
                                        Icon(name=icon_name, size=30),
                                        Text(
                                            value=f"{icon_name}",
                                            size=12,
                                            width=100,
                                            no_wrap=True,
                                            text_align="center",
                                            color=colors.ON_SURFACE_VARIANT,
                                        ),
                                    ],
                                    spacing=5,
                                    alignment="center",
                                    horizontal_alignment="center",
                                ),
                                alignment=alignment.center,
                            ),
                            tooltip=f"{icon_key}\nClick to copy to a clipboard",
                            on_click=copy_to_clipboard,
                            data=icon_key,
                        )
                    )
                status_bar.value = f"Icons found: {len(search_results.controls)}"
                self.update()

            if len(search_results.controls) == 0:
                self.page.show_snack_bar(SnackBar(Text("No icons found"), open=True))
            search_query.disabled = False
            self.update()

        return Column(
            [
                search_query,
                search_results,
                status_bar,
            ],
            expand=True,
        )


def main(page: Page):
    page.title = "Flet icons browser"
    page.add(IconBrowser(expand=True))


flet.app(target=main)
