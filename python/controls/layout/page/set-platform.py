import flet as ft


def main(page):
    def set_android(e):
        page.platform = ft.PagePlatform.ANDROID
        page.update()
        print("New platform:", page.platform)

    def set_ios(e):
        page.platform = "ios"
        page.update()
        print("New platform:", page.platform)

    page.add(
        ft.Switch(label="Switch A", adaptive=True),
        ft.ElevatedButton("Set Android", on_click=set_android),
        ft.ElevatedButton("Set iOS", on_click=set_ios),
    )

    print("Default platform:", page.platform)


ft.run(main)
