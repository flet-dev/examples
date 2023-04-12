import flet as ft

name = "ProgressRing Example"

def example():
    from time import sleep

    t = ft.Text(value="Click the button...")
    pr = ft.ProgressRing(width=16, height=16, stroke_width = 2)
    

    def button_clicked(e):
        t.value = "Doing something..."
        t.update()
        b.disabled = True
        b.update()
        for i in range(0, 101):
            pr.value = i * 0.01
            sleep(0.1)
            pr.update()
        t.value = "Click the button..."
        t.update()
        b.disabled = False
        b.update()

    b = ft.FilledTonalButton("Start", on_click=button_clicked)
    
    return ft.Column(
            [
                ft.Text("Circular progress indicator", style="headlineSmall"),
                ft.Row([pr, t]),
                ft.Text("Indeterminate cicrular progress", style="headlineSmall"),
                ft.Column(
                    [ft.ProgressRing(), ft.Text("I'm going to run for ages...")],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                b
            ],
            width=400,
            height=400
        )