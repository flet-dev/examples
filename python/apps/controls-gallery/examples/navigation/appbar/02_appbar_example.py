import flet as ft

def example2():
   pagelet = ft.Pagelet(
        appbar = ft.AppBar(
             title=ft.Text("TITLE", color=ft.Colors.WHITE),
             center_title=False,
             bgcolor=ft.Colors.BLACK,
             actions=[
               ft.TextButton("Category", width=140, icon=ft.icons.CATEGORY, icon_color=ft.Colors.WHITE,
                          style=ft.ButtonStyle(color=ft.Colors.WHITE,)),
               ft.TextButton("Recommend", width=200, icon=ft.icons.RECOMMEND, icon_color=ft.Colors.WHITE,
                          style=ft.ButtonStyle(color=ft.Colors.WHITE,)),
               ft.TextButton("Popularity", width=140, icon=ft.icons.FAVORITE, icon_color=ft.Colors.WHITE,
                          style=ft.ButtonStyle(color=ft.Colors.WHITE,)),
               ft.TextButton("Bads", icon=ft.icons.MOOD_BAD, width=140, icon_color=ft.Colors.WHITE,
                          style=ft.ButtonStyle(color=ft.Colors.WHITE,)),
               ft.TextButton("Favorites", width=140, icon=ft.icons.STAR_ROUNDED, icon_color=ft.Colors.WHITE,
                          style=ft.ButtonStyle(color=ft.Colors.WHITE,)),
               ft.Text("   ", width=265),
            ],
        ),
       content = ft.Container()
   )
   return pagelet
