import flet as ft

name = "Infinite scroll list"


def example():
    import threading

    class State:
        i = 0

    s = State()
    sem = threading.Semaphore()

    async def on_scroll(e: ft.OnScrollEvent):
        if e.pixels >= e.max_scroll_extent - 100:
            if sem.acquire(blocking=False):
                try:
                    for i in range(0, 10):
                        cl.controls.append(ft.Text(f"Text line {s.i}", key=str(s.i)))
                        s.i += 1
                    await cl.update_async()
                finally:
                    sem.release()

    cl = ft.Column(
        spacing=10,
        height=200,
        width=200,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
        on_scroll=on_scroll,
    )
    for i in range(0, 50):
        cl.controls.append(ft.Text(f"Text line {s.i}", key=str(s.i)))
        s.i += 1

    return ft.Container(cl, border=ft.border.all(1))
