import flet as ft


def main(page: ft.Page):
    page.padding = 50
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(
        ft.ElevatedButton(
            "Styled button 1",
            style=ft.ButtonStyle(
                color={
                    ft.ControlState.HOVERED: ft.colors.WHITE,
                    ft.ControlState.FOCUSED: ft.colors.BLUE,
                    ft.ControlState.DEFAULT: ft.colors.BLACK,
                },
                bgcolor={
                    ft.ControlState.FOCUSED: ft.colors.PINK_200,
                    ft.ControlState.DEFAULT: ft.colors.YELLOW,
                },
                padding={ft.ControlState.HOVERED: 20},
                overlay_color=ft.colors.TRANSPARENT,
                elevation={
                    ft.ControlState.DEFAULT: 0,
                    ft.ControlState.HOVERED: 5,
                    ft.ControlState.PRESSED: 10,
                },
                animation_duration=500,
                side={
                    ft.ControlState.DEFAULT: ft.BorderSide(1, color=ft.colors.BLUE_100),
                    ft.ControlState.HOVERED: ft.BorderSide(3, color=ft.colors.BLUE_400),
                    ft.ControlState.PRESSED: ft.BorderSide(6, color=ft.Colors.BLUE_600),
                },
                shape={
                    ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                    ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=2),
                },
            ),
        )
    )


ft.app(main)
