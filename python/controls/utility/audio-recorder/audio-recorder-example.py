import flet as ft

import flet_audio_recorder as ftar
import flet_audio as fta


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.appbar = ft.AppBar(title=ft.Text("Audio Recorder"), center_title=True)

    path = "test-audio-file.wav"

    def handle_start_recording(e):
        print(f"StartRecording: {path}")
        audio_rec.start_recording(path)

    def handle_stop_recording(e):
        output_path = audio_rec.stop_recording()
        print(f"StopRecording: {output_path}")
        log.value = f"StopRecording: {output_path}"
        if page.web and output_path is not None:
            page.launch_url(output_path)
        page.update()

    def handle_list_devices(e):
        devices = audio_rec.get_input_devices()
        print(devices)

    def handle_has_permission(e):
        try:
            print(f"HasPermission: {audio_rec.has_permission()}")
            log.value = f"HasPermission: {audio_rec.has_permission()}"
        except Exception as e:
            print(e)
        page.update()

    def handle_pause(e):
        print(f"isRecording: {audio_rec.is_recording()}")
        if audio_rec.is_recording():
            audio_rec.pause_recording()

    def handle_resume(e):
        print(f"isPaused: {audio_rec.is_paused()}")
        if audio_rec.is_paused():
            audio_rec.resume_recording()

    def handle_audio_encoding_test(e):
        for i in list(ft.AudioEncoder):
            print(f"{i}: {audio_rec.is_supported_encoder(i)}")
            page.add(ft.Text(f"audio encoder: {i.name}"))

    def handle_state_change(e):
        print(f"State Changed: {e.data}")

    audio_rec = ftar.AudioRecorder(
        # audio_encoder=ft.AudioEncoder.WAV,
        on_state_changed=handle_state_change,
    )
    audio_play = fta.Audio("non-existent", autoplay=False, volume=6)

    page.overlay.append(audio_play)

    def handle_start_play(e):
        page.add(ft.Text(f"play audio file: {audio_play.src}"))
        audio_play.src = "test-audio-file.wav"
        audio_play.update()
        audio_play.play()

    print(f"audio recorder: {audio_rec}")
    page.overlay.append(audio_rec)
    page.update()
    log = ft.Text(":")

    page.add(
        ft.ElevatedButton("Start Audio Recorder", on_click=handle_start_recording),
        ft.ElevatedButton("Stop Audio Recorder", on_click=handle_stop_recording),
        ft.ElevatedButton("List Devices", on_click=handle_list_devices),
        ft.ElevatedButton("Pause Recording", on_click=handle_pause),
        ft.ElevatedButton("Resume Recording", on_click=handle_resume),
        ft.ElevatedButton("Test AudioEncodings", on_click=handle_audio_encoding_test),
        ft.ElevatedButton("Has Permission", on_click=handle_has_permission),
        ft.ElevatedButton("Play", on_click=handle_start_play),
        ft.ElevatedButton("Pause", on_click=lambda _: audio_play.pause()),
        ft.ElevatedButton("Resume", on_click=lambda _: audio_play.resume()),
        ft.ElevatedButton("Release", on_click=lambda _: audio_play.release()),
        ft.ElevatedButton("Seek 2s", on_click=lambda _: audio_play.seek(2000)),
        log,
    )


ft.app(main)
