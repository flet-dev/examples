import flet as ft


def main(page: ft.Page):
    page.title = "Audio Example"

    def change_button(e):
        if e.state == ft.AudioState.PAUSED:
            b.text = "Resume playing"
            b.on_click = lambda e: audio1.resume()

        elif e.state == ft.AudioState.PLAYING:
            b.text = "Pause playing"
            b.on_click = lambda e: audio1.pause()

        b.update()

    audio1 = ft.Audio(
        src="https://luan.xyz/files/audio/ambient_c_motion.mp3",
        autoplay=True,
        on_state_changed=change_button,
    )
    b = ft.ElevatedButton("Pause playing", on_click=lambda _: audio1.pause())

    page.overlay.append(audio1)
    page.add(ft.Text("This is an app with background audio."), b)


ft.run(main)
