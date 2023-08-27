import flet as ft

name = "Autoplay Audio"


def example():
    class Example(ft.Column):
        def __init__(self):
            super().__init__()
            self.audio1 = ft.Audio(
                src="https://luan.xyz/files/audio/ambient_c_motion.mp3", autoplay=True
            )

            async def pause_audio(e):
                await self.audio1.pause_async()

            self.controls = [
                ft.Text(
                    "This is an app with background audio. Note: this example doesn't work in Safari browser."
                ),
                ft.ElevatedButton("Stop playing", on_click=pause_audio),
            ]

        # happens when example is added to the page (when user chooses the Audio control from the grid)
        async def did_mount_async(self):
            self.page.overlay.append(self.audio1)
            await self.page.update_async()

        # happens when example is removed from the page (when user chooses different control group on the navigation rail)
        async def will_unmount_async(self):
            self.page.overlay.remove(self.audio1)
            await self.page.update_async()

    audio_example = Example()

    return audio_example
