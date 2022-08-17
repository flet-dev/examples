import time

import flet
from flet import AnimatedSwitcher, ElevatedButton, Image, Page


def main(page: Page):

    i = Image(src="https://picsum.photos/200/300", width=200, height=300)

    def animate(e):
        sw.content = Image(
            src=f"https://picsum.photos/200/300?{time.time()}", width=200, height=300
        )
        page.update()

    sw = AnimatedSwitcher(
        i,
        transition="scale",
        duration=500,
        reverse_duration=100,
        switch_in_curve="bounceOut",
        switch_out_curve="bounceIn",
    )

    page.add(
        sw,
        ElevatedButton("Animate!", on_click=animate),
    )


flet.app(target=main)
