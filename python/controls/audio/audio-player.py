import logging

import flet
from flet import Audio, ElevatedButton, Page, Row, Text

# logging.basicConfig(level=logging.DEBUG)

# url = "https://github.com/mdn/webaudio-examples/blob/main/audio-basics/outfoxing.mp3?raw=true"
url = "https://github.com/mdn/webaudio-examples/blob/main/audio-analyser/viper.mp3?raw=true"
# url = "https://luan.xyz/files/audio/ambient_c_motion.mp3"
# url = "https://luan.xyz/files/audio/coins.wav"
# url = "https://luan.xyz/files/audio/laser.wav"


def main(page: Page):
    def volume_down(_):
        audio1.volume -= 0.1
        audio1.update()

    def volume_up(_):
        audio1.volume += 0.1
        audio1.update()

    def balance_left(_):
        audio1.balance -= 0.1
        audio1.update()

    def balance_right(_):
        audio1.balance += 0.1
        audio1.update()

    audio1 = Audio(
        src=url,
        autoplay=False,
        volume=1,
        balance=0,
        on_loaded=lambda _: print("Loaded"),
        on_duration_changed=lambda e: print("Duration changed:", e.data),
        on_position_changed=lambda e: print("Position changed:", e.data),
        on_state_changed=lambda e: print("State changed:", e.data),
        on_seek_complete=lambda _: print("Seek complete"),
    )
    page.overlay.append(audio1)
    page.add(
        ElevatedButton("Play", on_click=lambda _: audio1.play()),
        ElevatedButton("Pause", on_click=lambda _: audio1.pause()),
        ElevatedButton("Resume", on_click=lambda _: audio1.resume()),
        ElevatedButton("Release", on_click=lambda _: audio1.release()),
        ElevatedButton("Seek 2s", on_click=lambda _: audio1.seek(2000)),
        Row(
            [
                ElevatedButton("Volume down", on_click=volume_down),
                ElevatedButton("Volume up", on_click=volume_up),
            ]
        ),
        Row(
            [
                ElevatedButton("Balance left", on_click=balance_left),
                ElevatedButton("Balance right", on_click=balance_right),
            ]
        ),
        ElevatedButton(
            "Get duration", on_click=lambda _: print("Duration:", audio1.get_duration())
        ),
        ElevatedButton(
            "Get current position",
            on_click=lambda _: print("Current position:", audio1.get_duration()),
        ),
    )


flet.app(target=main)
