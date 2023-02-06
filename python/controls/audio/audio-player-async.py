import flet as ft


url = "https://github.com/mdn/webaudio-examples/blob/main/audio-analyser/viper.mp3?raw=true"


async def main(page: ft.Page):
    async def volume_down(_):
        audio1.volume -= 0.1
        await audio1.update_async()

    async def volume_up(_):
        audio1.volume += 0.1
        await audio1.update_async()

    async def balance_left(_):
        audio1.balance -= 0.1
        await audio1.update_async()

    async def balance_right(_):
        audio1.balance += 0.1
        await audio1.update_async()

    async def play(_):
        await audio1.play_async()

    async def pause(_):
        await audio1.pause_async()

    async def resume(_):
        await audio1.resume_async()

    async def release(_):
        await audio1.release_async()

    async def seek(_):
        await audio1.seek_async(2000)

    async def get_duration(_):
        print("Current position:", await audio1.get_duration_async())

    audio1 = ft.Audio(
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
    await page.add_async(
        ft.ElevatedButton("Play", on_click=play),
        ft.ElevatedButton("Pause", on_click=pause),
        ft.ElevatedButton("Resume", on_click=resume),
        ft.ElevatedButton("Release", on_click=release),
        ft.ElevatedButton("Seek 2s", on_click=seek),
        ft.Row(
            [
                ft.ElevatedButton("Volume down", on_click=volume_down),
                ft.ElevatedButton("Volume up", on_click=volume_up),
            ]
        ),
        ft.Row(
            [
                ft.ElevatedButton("Balance left", on_click=balance_left),
                ft.ElevatedButton("Balance right", on_click=balance_right),
            ]
        ),
        ft.ElevatedButton("Get duration", on_click=get_duration),
        ft.ElevatedButton(
            "Get current position",
            on_click=get_duration,
        ),
    )


ft.app(main)
