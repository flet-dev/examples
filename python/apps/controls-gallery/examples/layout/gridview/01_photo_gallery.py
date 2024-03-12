import flet as ft

name = "GridView Example"

def example():
    
    images = ft.GridView(
        height=400,
        width=400,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    for i in range(0, 60):
        images.controls.append(
            ft.Image(
                src=f"https://picsum.photos/150/150?{i}",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )

    return images