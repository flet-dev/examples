import flet as ft

name = "Pre-defined theme text styles"

def example():
    
    return ft.Column(
        controls=[
        ft.Text("Display Large", style=ft.TextThemeStyle.DISPLAY_LARGE),
        ft.Text("Display Medium", style=ft.TextThemeStyle.DISPLAY_MEDIUM),
        ft.Text("Display Small", style=ft.TextThemeStyle.DISPLAY_SMALL),
        ft.Text("Headline Large", style=ft.TextThemeStyle.HEADLINE_LARGE),
        ft.Text("Headline Medium", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        ft.Text("Headline Small", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        ft.Text("Title Large", style=ft.TextThemeStyle.TITLE_LARGE),
        ft.Text("Title Medium", style=ft.TextThemeStyle.TITLE_MEDIUM),
        ft.Text("Title Small", style=ft.TextThemeStyle.TITLE_SMALL),
        ft.Text("Label Large", style=ft.TextThemeStyle.LABEL_LARGE),
        ft.Text("Label Medium", style=ft.TextThemeStyle.LABEL_MEDIUM),
        ft.Text("Label Small", style=ft.TextThemeStyle.LABEL_SMALL),
        ft.Text("Body Large", style=ft.TextThemeStyle.BODY_LARGE),
        ft.Text("Body Medium", style=ft.TextThemeStyle.BODY_MEDIUM),
        ft.Text("Body Small", style=ft.TextThemeStyle.BODY_SMALL)
    ])