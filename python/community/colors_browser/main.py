import os
import time
from itertools import islice

import flet
from flet import (
    Column,
    Container,
    GridView,
    Icon,
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
    FloatingActionButton, IconButton, ProgressBar, ButtonStyle
)

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "6000000"

class ColorBrowser(UserControl):
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
        colors_list = []
        list_started = False
        for key, value in vars(colors).items():
            if key == "PRIMARY":
                # 'PRIMARY' is the first color-variable (our starting point)
                list_started = True
            if list_started:
                # when this bool variable is True, we can start appending the variables in our list
                colors_list.append(key.lower())

        search_txt = TextField(
            expand=1, hint_text="Enter keyword and press search button", autofocus=True,
            on_submit=lambda e: display_colors(e.control.value), tooltip="search field"
        )

        def search_click(e):
            """
            Called when the search button is pressed, it displays the colors.
            """
            display_colors(search_txt.value)

        search_query = Row(
            [search_txt, FloatingActionButton(icon=icons.SEARCH, on_click=search_click, tooltip="search")]
        )

        search_results = GridView(
            expand=1, runs_count=10, max_extent=150, spacing=5, run_spacing=5, child_aspect_ratio=1,
        )
        status_bar = Text()

        def copy_to_clipboard(e):
            """copies the color code to the clipboard"""
            color_key = e.control.data
            print("Copy to clipboard:", color_key)
            self.page.set_clipboard(e.control.data)
            self.page.show_snack_bar(SnackBar(Text(f"Copied {color_key}"), open=True))

        def search_colors(search_term: str):
            if search_term != "":
                # if the sea
                for color_name in colors_list:
                    if search_term in color_name:
                        yield color_name

        def display_colors(search_term: str):
            """Gets the search term and tries to display the colors in the grid view"""

            # clean search results
            search_query.disabled = True
            self.update()
            search_results.clean()

            for batch in batches(search_colors(search_term.lower()), 40):
                for color_name in batch:
                    color_key = f"colors.{color_name.upper()}"

                    search_results.controls.append(
                        TextButton(
                            content=Container(
                                content=Column(
                                    [
                                        Icon(name=icons.RECTANGLE, size=38, color=color_name, ),
                                        Text(
                                            value=f"{color_name}", size=14, width=100,
                                            no_wrap=True, text_align="center", color=color_name,
                                        ),
                                    ],
                                    spacing=5,
                                    alignment="center",
                                    horizontal_alignment="center",
                                ),
                                alignment=alignment.center,
                            ),
                            tooltip=f"{color_key}\nClick to copy to a clipboard",
                            on_click=copy_to_clipboard,
                            data=color_key,
                        )
                    )
                status_bar.value = f"Colors found: {len(search_results.controls)}"
                self.update()

            if len(search_results.controls) == 0:
                # if no color was found containing the user's search term
                self.page.show_snack_bar(SnackBar(Text("No colors found"), open=True))
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
    page.title = "Flet colors browser"
    # page.window_always_on_top = True
    page.theme_mode = "dark"

    def change_theme(e):
        """
        Changes the theme_mode and displays a progressbar while doing this.
        :param e: the event toggler
        :type e: ControlEvent
        """
        p_bar.visible = True
        page.update()
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        p_bar.visible = False
        theme_button.selected = not theme_button.selected
        time.sleep(1.2)
        page.update()

    # a progress bar shown when changing theme
    p_bar = ProgressBar(bar_height=3.5, visible=False)
    # theme changer button
    theme_button = IconButton(icons.LIGHT_MODE, on_click=change_theme, icon_size=40, selected_icon=icons.DARK_MODE,
                              tooltip="change theme",
                              style=ButtonStyle(color={"selected": colors.BLACK, "": colors.WHITE}))

    page.add(
        p_bar,
        Row(controls=[Text("Flet Color Browser", style="displayMedium", color=colors.BLUE),
                      theme_button], alignment="spaceAround"),
        ColorBrowser(expand=True)
    )


flet.app(target=main)
# OR flet.app(target=main, view=flet.WEB_BROWSER, port=5050) then open http://localhost:5050/
