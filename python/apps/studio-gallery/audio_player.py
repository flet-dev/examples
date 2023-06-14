import flet as ft


def example():
    import flet.canvas as cv

    url = "https://github.com/mdn/webaudio-examples/blob/main/audio-analyser/viper.mp3?raw=true"

    def convertMillis(millis):
        seconds = int(millis / 1000) % 60
        minutes = int(millis / (1000 * 60)) % 60
        return f"{minutes}:{seconds}"

    class Track(ft.GestureDetector):
        def __init__(self, audio):
            super().__init__()
            self.content = ft.Stack(
                expand=True,
                height=6,
                controls=[
                    ft.Container(expand=True, border_radius=3, bgcolor=ft.colors.BLACK)
                ],
            )
            self.audio = audio
            # self.duration = duration
            self.on_pan_start = self.find_position
            self.on_hover = self.change_cursor

        def find_position(self, e: ft.DragStartEvent):
            print(f"Total track width: {self.content.width}")
            print(f"Total track duration: {convertMillis(self.audio.get_duration())}")
            print(
                f"Position: {convertMillis(self.audio.get_duration()*e.local_x/e.control.page.width)}"
            )
            print(e.control.content.controls[0].width)

        def change_cursor(self, e: ft.HoverEvent):
            e.control.mouse_cursor = ft.MouseCursor.CLICK
            e.control.update()

    class TrackCanvas(ft.GestureDetector):
        def __init__(self, audio):
            super().__init__()
            self.content = ft.Container(
                content=cv.Canvas(
                    on_resize=self.canvas_resized,
                    shapes=[
                        cv.Rect(
                            x=0,
                            y=0,
                            height=5,
                            border_radius=3,
                            paint=ft.Paint(color="black"),
                            width=100,
                        )
                    ],
                ),
                height=10,
                width=float("inf"),
            )
            self.audio = audio
            # self.duration = duration
            self.on_pan_start = self.find_position
            self.on_hover = self.change_cursor

        def canvas_resized(self, e: cv.CanvasResizeEvent):
            print("On resize:", e.width, e.height)
            self.track_width = e.width
            e.control.shapes[0].width = e.width
            e.control.update()

        def find_position(self, e: ft.DragStartEvent):
            print(f"Total track width: {self.content.width}")
            print(f"Total track duration: {convertMillis(self.audio.get_duration())}")
            print(
                f"Position: {convertMillis(self.audio.get_duration()*e.local_x/e.control.page.width)}"
            )
            # print(e.control.content.controls[0].width)

        def change_cursor(self, e: ft.HoverEvent):
            e.control.mouse_cursor = ft.MouseCursor.CLICK
            e.control.update()

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
            self.track_canvas = TrackCanvas(audio=self.audio1)
            self.track = Track(audio=self.audio1)
            self.controls = [
                self.track_canvas,
                # self.track,
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
