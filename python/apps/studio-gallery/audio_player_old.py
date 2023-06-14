import flet as ft


def example():
    url = "https://github.com/mdn/webaudio-examples/blob/main/audio-analyser/viper.mp3?raw=true"

    class Example(ft.Column):
        def __init__(self):
            super().__init__()
            self.audio1 = ft.Audio(
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

            self.controls = [
                ft.ElevatedButton("Play", on_click=lambda _: self.audio1.play()),
                ft.ElevatedButton("Pause", on_click=lambda _: self.audio1.pause()),
                ft.ElevatedButton("Resume", on_click=lambda _: self.audio1.resume()),
                ft.ElevatedButton("Release", on_click=lambda _: self.audio1.release()),
                ft.ElevatedButton("Seek 2s", on_click=lambda _: self.audio1.seek(2000)),
                ft.Row(
                    [
                        ft.ElevatedButton("Volume down", on_click=self.volume_down),
                        ft.ElevatedButton("Volume up", on_click=self.volume_up),
                    ]
                ),
                ft.Row(
                    [
                        ft.ElevatedButton("Balance left", on_click=self.balance_left),
                        ft.ElevatedButton("Balance right", on_click=self.balance_right),
                    ]
                ),
                ft.ElevatedButton(
                    "Get duration",
                    on_click=lambda _: print("Duration:", self.audio1.get_duration()),
                ),
                ft.ElevatedButton(
                    "Get current position",
                    on_click=lambda _: print(
                        "Current position:", self.audio1.get_duration()
                    ),
                ),
            ]

        # happens when example is added to the page (when user chooses the Audio control from the grid)
        def did_mount(self):
            self.page.overlay.append(self.audio1)
            self.page.update()

        # happens when example is removed from the page (when user chooses different control group on the navigation rail)
        def will_unmount(self):
            self.page.overlay.remove(self.audio1)
            self.page.update()

        def volume_down(self, _):
            self.audio1.volume -= 0.1
            self.audio1.update()

        def volume_up(self, _):
            self.audio1.volume += 0.1
            self.audio1.update()

        def balance_left(self, _):
            self.audio1.balance -= 0.1
            self.audio1.update()

        def balance_right(self, _):
            self.audio1.balance += 0.1
            self.audio1.update()

    example_column = Example()

    return example_column


def main(page: ft.Page):
    page.title = "Flet audio player example"
    page.window_width = 390
    page.window_height = 844
    page.add(example())


if __name__ == "__main__":
    ft.app(target=main)
