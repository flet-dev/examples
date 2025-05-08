import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    i = 1

    img_container = ft.Container(
        image=ft.DecorationImage(src="https://picsum.photos/250/250"),
        width=250,
        height=250,
    )

    def change_img(e):
        nonlocal i
        print(f"button clicked {i}")
        img_container.image = ft.DecorationImage(
            src=f"https://picsum.photos/250/250?random={i}"
        )
        i += 1
        page.update()

    page.add(
        ft.Stack(
            [
                img_container,
                ft.Container(
                    width=100,
                    height=100,
                    blur=10,
                    bgcolor="#22CCCC00",
                ),
                ft.Container(
                    width=100,
                    height=100,
                    left=20,
                    top=120,
                    blur=(0, 10),
                ),
                ft.Container(
                    top=50,
                    right=10,
                    blur=ft.Blur(10, 0, ft.BlurTileMode.MIRROR),
                    width=100,
                    height=100,
                    bgcolor="#44CCCCCC",
                    border_radius=10,
                    border=ft.border.all(2, ft.Colors.BLACK),
                ),
                ft.ElevatedButton(
                    content="Change Background",
                    bottom=5,
                    right=5,
                    style=ft.ButtonStyle(text_style=ft.TextStyle(size=8)),
                    on_click=change_img,
                ),
            ]
        )
    )


ft.run(main)
