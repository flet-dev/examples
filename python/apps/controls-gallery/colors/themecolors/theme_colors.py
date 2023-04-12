import flet as ft

name = "Theme colors"

def example():

    return ft.ListView(width=500, spacing=10, padding=20, auto_scroll=True, controls=[
        ft.Container(
            border_radius=10,
            #border=ft.border.all(1, ft.colors.ON_SECONDARY_CONTAINER),
            #margin=10,
            #padding=10,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.PRIMARY, 
                        content=ft.Text("PRIMARY"), 
                        alignment = ft.alignment.center, 
                        border_radius=ft.border_radius.only(topLeft=10, topRight=10)
                        ),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.ON_PRIMARY, 
                        content=ft.Text("ON_PRIMARY"), 
                        alignment = ft.alignment.center),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.PRIMARY_CONTAINER, 
                        content=ft.Text("PRIMARY_CONTAINER"), 
                        alignment = ft.alignment.center),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.ON_PRIMARY_CONTAINER, 
                        content=ft.Text("ON_PRIMARY_CONTAINER"), 
                        alignment = ft.alignment.center,
                        border_radius=ft.border_radius.only(bottomLeft=10, bottomRight=10)
                    )
                ])),
        ft.Container(
            border_radius=10,
            #border=ft.border.all(1, ft.colors.ON_SECONDARY_CONTAINER),
            #margin=10,
            #padding=10,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.SECONDARY, 
                        content=ft.Text("SECONDARY"), 
                        alignment = ft.alignment.center, 
                        border_radius=ft.border_radius.only(topLeft=10, topRight=10)
                        ),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.ON_SECONDARY, 
                        content=ft.Text("ON_SECONDARY"), 
                        alignment = ft.alignment.center),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.SECONDARY_CONTAINER, 
                        content=ft.Text("SECONDARY_CONTAINER"), 
                        alignment = ft.alignment.center),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.ON_SECONDARY_CONTAINER, 
                        content=ft.Text("ON_SECONDARY_CONTAINER"), 
                        alignment = ft.alignment.center,
                        border_radius=ft.border_radius.only(bottomLeft=10, bottomRight=10)
                    )
                ])),
        ft.Container(
            border_radius=10,
            #border=ft.border.all(1, ft.colors.ON_SECONDARY_CONTAINER),
            #margin=10,
            #padding=10,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.TERTIARY, 
                        content=ft.Text("TERTIARY"), 
                        alignment = ft.alignment.center, 
                        border_radius=ft.border_radius.only(topLeft=10, topRight=10)
                        ),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.ON_TERTIARY, 
                        content=ft.Text("ON_TERTIARY"), 
                        alignment = ft.alignment.center),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.TERTIARY_CONTAINER, 
                        content=ft.Text("TERTIARY_CONTAINER"), 
                        alignment = ft.alignment.center),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.ON_TERTIARY_CONTAINER, 
                        content=ft.Text("ON_TERTIARY_CONTAINER"), 
                        alignment = ft.alignment.center,
                        border_radius=ft.border_radius.only(bottomLeft=10, bottomRight=10)
                    )
                ])),
        ft.Container(
            border_radius=10,
            #border=ft.border.all(1, ft.colors.ON_SECONDARY_CONTAINER),
            #margin=10,
            #padding=10,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.ERROR, 
                        content=ft.Text("ERROR"), 
                        alignment = ft.alignment.center, 
                        border_radius=ft.border_radius.only(topLeft=10, topRight=10)
                        ),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.ON_ERROR, 
                        content=ft.Text("ON_ERROR"), 
                        alignment = ft.alignment.center),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.ERROR_CONTAINER, 
                        content=ft.Text("ERROR_CONTAINER"), 
                        alignment = ft.alignment.center),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.ON_ERROR_CONTAINER, 
                        content=ft.Text("ON_ERROR_CONTAINER"), 
                        alignment = ft.alignment.center,
                        border_radius=ft.border_radius.only(bottomLeft=10, bottomRight=10)
                    )
                ])),
        ft.Container(
            border_radius=10,
            #border=ft.border.all(1, ft.colors.ON_SECONDARY_CONTAINER),
            #margin=10,
            #padding=10,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.BACKGROUND, 
                        content=ft.Text("BACKGROUND"), 
                        alignment = ft.alignment.center, 
                        border_radius=ft.border_radius.only(topLeft=10, topRight=10)
                        ),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.ON_BACKGROUND, 
                        content=ft.Text("ON_BACKGROUND"), 
                        alignment = ft.alignment.center,
                        border_radius=ft.border_radius.only(bottomLeft=10, bottomRight=10)
                    )
                ])),
        ft.Container(
            border_radius=10,
            #border=ft.border.all(1, ft.colors.ON_SECONDARY_CONTAINER),
            #margin=10,
            #padding=10,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.SURFACE, 
                        content=ft.Text("SURFACE"), 
                        alignment = ft.alignment.center, 
                        border_radius=ft.border_radius.only(topLeft=10, topRight=10)
                        ),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.ON_SURFACE, 
                        content=ft.Text("ON_SURFACE"), 
                        alignment = ft.alignment.center),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.SURFACE_VARIANT, 
                        content=ft.Text("SURFACE_VARIANT"), 
                        alignment = ft.alignment.center),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.ON_SURFACE_VARIANT, 
                        content=ft.Text("ON_SURFACE_VARIANT"), 
                        alignment = ft.alignment.center,
                        border_radius=ft.border_radius.only(bottomLeft=10, bottomRight=10)
                    )
                ])),
        ft.Container(
            border_radius=10,
            #border=ft.border.all(1, ft.colors.ON_SECONDARY_CONTAINER),
            #margin=10,
            #padding=10,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.OUTLINE, 
                        content=ft.Text("OUTLINE"), 
                        alignment = ft.alignment.center, 
                        border_radius=ft.border_radius.only(topLeft=10, topRight=10)
                        ),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.SHADOW, 
                        content=ft.Text("SHADOW"), 
                        alignment = ft.alignment.center),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.INVERSE_SURFACE, 
                        content=ft.Text("INVERSE_SURFACE"), 
                        alignment = ft.alignment.center),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.ON_INVERSE_SURFACE, 
                        content=ft.Text("ON_INVERSE_SURFACE"), 
                        alignment = ft.alignment.center),
                    ft.Container(
                        height=50, 
                        bgcolor=ft.colors.INVERSE_PRIMARY, 
                        content=ft.Text("INVERSE_PRIMARY"), 
                        alignment = ft.alignment.center,
                        border_radius=ft.border_radius.only(bottomLeft=10, bottomRight=10)
                    )
                ]))

    ])