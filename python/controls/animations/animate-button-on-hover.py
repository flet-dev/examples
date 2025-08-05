import flet as ft


def main(page: ft.Page):

    def animate(e):
        b.rotate = 0.1 if e.data == "true" else 0
        page.update()

    t = ft.Text()
    b = ft.ElevatedButton(
        "Hover over me, I'm animated!",
        rotate=0,
        animate_rotation=100,
        on_hover=animate,
        on_click=lambda e: page.add(ft.Text("Clicked! Try a long press!")),
        on_long_press=lambda e: page.add(ft.Text("I knew you could do it!")),
    )

    page.add(b)


ft.run(main)
