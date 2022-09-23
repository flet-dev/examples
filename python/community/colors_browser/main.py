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

# Increasing the maximum message size that can be sent over the websocket.
os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "6000000"

class ColorBrowser(UserControl):
    def __init__(self, expand=False, height=500):
        """
        If the expand parameter is set to True, then the expand attribute of the object is set to True. Otherwise, the
        height attribute of the object is set to the value of the height parameter.

        :param expand: If True, the widget will expand to fill its parent, defaults to False (optional)
        :param height: The height of the widget, defaults to 500 (optional)
        """
        super().__init__()
        if expand:
            self.expand = expand
        else:
            self.height = height

    def build(self):
        def batches(iterable, batch_size):
            """
            It takes an iterable and a batch size, and returns an iterator that yields batches of the iterable

            :param iterable: An iterable object (e.g. a list)
            :param batch_size: The number of items to process in each batch
            """
            iterator = iter(iterable)
            while batch := list(islice(iterator, batch_size)):
                yield batch

        # fetch all icon constants from colors.py module and store them in a dict(colors_dict)
        colors_dict = dict()
        list_started = False
        for key, value in vars(colors).items():
            if key == "PRIMARY":
                # 'PRIMARY' is the first color-variable (our starting point)
                list_started = True
            if list_started:
                # when this list_started is True, we create new key-value pair in our dictionary
                colors_dict[key] = value

        # Creating a text field
        search_txt = TextField(
            expand=1, hint_text="Enter keyword and press search button", autofocus=True,
            on_submit=lambda e: display_colors(e.control.value), tooltip="search field"
        )

        def search_click(e):
            """
            Called when the search button is pressed, it displays the colors.
            """
            display_colors(search_txt.value)

        # Creating a row with a search text field and a search button.
        search_query = Row(
            [search_txt, FloatingActionButton(icon=icons.SEARCH, on_click=search_click, tooltip="search")]
        )

        # Creating a grid view with 10 columns and 150 pixels as the maximum extent of each column.
        search_results = GridView(
            expand=1, runs_count=10, max_extent=150, spacing=5, run_spacing=5, child_aspect_ratio=1,
        )
        status_bar = Text()

        def copy_to_clipboard(e):
            """
            When the user clicks on a color, copy the color key to the clipboard

            :param e: The event object
            """

            color_key = e.control.data
            print("Copy to clipboard:", color_key)
            self.page.set_clipboard(e.control.data)
            self.page.show_snack_bar(SnackBar(Text(f"Copied {color_key}"), open=True))

        def search_colors(search_term: str):
            """
            It takes a search term as an argument, and then loops through the colors_dict dictionary,
            checking if the search term is in the color name or the color value. If it is, it yields the color key

            :param search_term: The search term that the user entered
            :return color_key: str
            """

            for color_key, color_value in colors_dict.items():
                # the color_key has underscores while the color_value doesn't. We take this into consideration
                if search_term and (search_term in color_value or search_term in color_key.lower()):
                    yield color_key

        def display_colors(search_term: str):
            """
            It takes a search term, disables the search box, cleans the search results(grid view),
            and then loops through the search results in batches of 40, adding each color to the search results

            :param search_term: str
            """

            # disable the text field and the search button, and clean search results
            search_query.disabled = True
            self.update()
            search_results.clean()

            # Adding the colors to the grid view in batches of 40.
            for batch in batches(search_colors(search_term.lower()), 40):
                for color_key in batch:
                    flet_color_key = f"colors.{color_key}"

                    search_results.controls.append(
                        TextButton(
                            content=Container(
                                content=Column(
                                    [
                                        Icon(name=icons.RECTANGLE, size=38, color=colors_dict[color_key], ),
                                        Text(
                                            value=f"{colors_dict[color_key]}", size=14, width=100,
                                            no_wrap=True, text_align="center", color=colors_dict[color_key],
                                        ),
                                    ],
                                    spacing=5,
                                    alignment="center",
                                    horizontal_alignment="center",
                                ),
                                alignment=alignment.center,
                            ),
                            tooltip=f"{flet_color_key}\nClick to copy to a clipboard",
                            on_click=copy_to_clipboard,
                            data=flet_color_key,
                        )
                    )
                status_bar.value = f"Colors found: {len(search_results.controls)}"
                self.update()

            # It checks if the search results are empty, and if they are, it shows a snack bar some message
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
        When the button(to change theme) is clicked, the progress bar is made visible, the theme is changed,
        the progress bar is made invisible, and the page is updated

        :param e: The event that triggered the function
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
    # button to change theme_mode (from dark to light mode, or the reverse)
    theme_button = IconButton(icons.LIGHT_MODE, on_click=change_theme, icon_size=40, selected_icon=icons.DARK_MODE,
                              tooltip="change theme",
                              style=ButtonStyle(color={"selected": colors.BLACK, "": colors.WHITE}))

    page.add(
        p_bar,
        Row(controls=[Text("Flet Color Browser", style="displayMedium", color=colors.BLUE),
                      theme_button], alignment="spaceAround"),
        ColorBrowser(expand=True)
    )


# Creating a web server and a web socket server (running the app)
flet.app(target=main)
# OR flet.app(target=main, view=flet.WEB_BROWSER, port=5050) then open http://localhost:5050/
