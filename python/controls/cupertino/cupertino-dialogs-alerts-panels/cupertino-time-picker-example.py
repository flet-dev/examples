import time
import flet as ft


def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    timer_picker_value_ref = ft.Ref[ft.Text]()

    def handle_timer_picker_change(e):
        print(f"time in seconds: {e.data.in_seconds}")
        print(f"time in minutes:{e.data.in_minutes}")
        print(f"time in hours:{e.data.in_hours}")
        # t = time.struct_time(tm_hour=e.data.in_hours)
        # e.data is the selected time in seconds
        # timer_picker_value_ref.current.value = time.strftime("%H:%M:%S", (e.data.)
        timer_picker_value_ref.current.value = f"{e.data.in_hours}:{(e.data.in_minutes % 60)}:{(e.data.in_seconds % 60) % 60}"

        page.update()

    cupertino_timer_picker = ft.CupertinoTimerPicker(
        # value=ft.DurationValue(),
        second_interval=10,
        minute_interval=1,
        mode=ft.CupertinoTimerPickerMode.HOUR_MINUTE_SECONDS,
        on_change=handle_timer_picker_change,
    )

    page.add(
        ft.Row(
            tight=True,
            controls=[
                ft.Text("TimerPicker Value:", size=23),
                ft.CupertinoButton(
                    content=ft.Text(
                        ref=timer_picker_value_ref,
                        value="00:01:10",
                        size=23,
                        color=ft.CupertinoColors.DESTRUCTIVE_RED,
                    ),
                    on_click=lambda e: page.show_dialog(
                        ft.CupertinoBottomSheet(
                            cupertino_timer_picker,
                            height=216,
                            padding=ft.padding.only(top=6),
                        )
                    ),
                ),
            ],
        ),
    )


ft.run(main)
