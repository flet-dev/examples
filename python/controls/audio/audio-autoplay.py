import flet
from flet import Audio, ElevatedButton, Page, Text


def main(page: Page):
    audio1 = Audio(
        src="https://luan.xyz/files/audio/ambient_c_motion.mp3", autoplay=True
    )
    page.overlay.append(audio1)
    page.add(
        Text("This is an app with background audio."),
        ElevatedButton("Stop playing", on_click=lambda _: audio1.pause()),
    )


flet.app(target=main)
