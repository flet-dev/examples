import flet as ft
from solitaire import Solitaire


async def main(page: ft.Page):

    page.on_error = lambda e: print("Page error:", e.data)

    solitaire = Solitaire()

    await page.add_async(solitaire)


ft.app(target=main, assets_dir="assets")
