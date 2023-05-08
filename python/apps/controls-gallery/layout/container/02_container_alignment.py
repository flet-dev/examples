import flet as ft

name = "Containers with different alignment"

def example():

    container_1 = ft.Container(
        content=ft.Text("Center"), 
        alignment=ft.alignment.center, 
        bgcolor=ft.colors.BLUE_GREY_100,
        width=150,
        height=150)

    container_2 = ft.Container(
        content=ft.Text("Top left"), 
        alignment=ft.alignment.top_left, 
        bgcolor=ft.colors.BLUE_GREY_200,
        width=150,
        height=150)

    container_3 = ft.Container(
        content=ft.Text("-0.5, -0.5"), 
        alignment=ft.alignment.Alignment(-0.5, -0.5), 
        bgcolor=ft.colors.BLUE_GREY_300,
        width=150,
        height=150)

    return ft.Row(controls=[
        container_1,
        container_2,
        container_3
        ]
    )