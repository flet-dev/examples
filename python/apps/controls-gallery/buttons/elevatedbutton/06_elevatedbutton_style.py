import flet as ft

name = "ElevatedButton with style attributes configured for different MaterialState values"

def example():
    
    return ft.ElevatedButton(
            "Styled button 1",
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.HOVERED: ft.colors.WHITE,
                    ft.MaterialState.FOCUSED: ft.colors.BLUE,
                    ft.MaterialState.DEFAULT: ft.colors.BLACK,
                },
                bgcolor={ft.MaterialState.FOCUSED: ft.colors.PINK_200, "": ft.colors.YELLOW},
                padding={ft.MaterialState.HOVERED: 20},
                overlay_color=ft.colors.TRANSPARENT,
                elevation={"pressed": 0, "": 1},
                animation_duration=500,
                side={
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                    ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.BLUE),
                },
                shape={
                    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=2),
                },
            ),
        )