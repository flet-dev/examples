import flet as ft


def example():
    import flet.canvas as cv

    url = "https://github.com/mdn/webaudio-examples/blob/main/audio-analyser/viper.mp3?raw=true"

    def convertMillis(millis):
        seconds = int(millis / 1000) % 60
        if seconds < 10:
            seconds_str = f"0{seconds}"
        else:
            seconds_str = f"{seconds}"
        minutes = int(millis / (1000 * 60)) % 60
        return f"{minutes}:{seconds_str}"

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
                f"Position: {convertMillis(self.audio.get_duration()*e.local_x/self.track_width)}"
            )
            return self.audio.get_duration() * e.local_x / self.track_width
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
                on_position_changed=self.change_position,
                on_state_changed=self.state_changed,
                on_seek_complete=lambda _: print("Seek complete"),
            )
            self.state = None
            self.track_canvas = TrackCanvas(audio=self.audio1)
            self.play_button = ft.IconButton(
                icon=ft.icons.PLAY_ARROW,
                visible=False,
                on_click=self.play,
            )
            self.pause_button = ft.IconButton(
                icon=ft.icons.PAUSE,
                visible=False,
                on_click=self.pause,
            )
            self.position_duration = ft.Text()
            self.controls = [
                self.track_canvas,
                ft.Row(
                    controls=[
                        self.play_button,
                        self.pause_button,
                        self.position_duration,
                    ]
                ),
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
            self.position_duration.value = (
                f"{convertMillis(0)} / {convertMillis(self.audio1.get_duration())}"
            )
            self.play_button.visible = True
            self.page.update()

        # happens when example is removed from the page (when user chooses different control group on the navigation rail)
        def will_unmount(self):
            self.page.overlay.remove(self.audio1)
            self.page.update()

        def play(self, e):
            print(self.state)
            if self.state == "paused":
                self.audio1.resume()

            else:
                self.audio1.play()
            self.play_button.visible = False
            self.pause_button.visible = True
            self.page.update()

        def pause(self, e):
            self.audio1.pause()
            self.play_button.visible = True
            self.pause_button.visible = False
            self.page.update()

        def state_changed(self, e):
            self.state = e.data

        def change_position(self, e):
            print("Position changed:", e.data)
            self.position_duration.value = f"{convertMillis(int(e.data))} / {convertMillis(self.audio1.get_duration())}"
            e.control.page.update()

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
