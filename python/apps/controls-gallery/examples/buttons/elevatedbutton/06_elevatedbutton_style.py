import flet as ft

name = (
    "ElevatedButton with style attributes configured for different ControlState values"
)


def example():

    return ft.ElevatedButton(
        "Styled button 1",
        style=ft.ButtonStyle(
            color={
                ft.ControlState.HOVERED: ft.colors.WHITE,
                ft.ControlState.FOCUSED: ft.colors.BLUE,
                ft.ControlState.DEFAULT: ft.colors.BLACK,
            },
            bgcolor={ft.ControlState.FOCUSED: ft.colors.PINK_200, "": ft.colors.YELLOW},
            padding={ft.ControlState.HOVERED: 20},
            overlay_color=ft.colors.TRANSPARENT,
            elevation={"pressed": 0, "": 1},
            animation_duration=500,
            side={
                ft.ControlState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                ft.ControlState.HOVERED: ft.BorderSide(2, ft.colors.BLUE),
            },
            shape={
                ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=2),
            },
        ),
    )
