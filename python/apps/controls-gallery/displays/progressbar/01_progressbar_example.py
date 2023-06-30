import flet as ft

name = "ProgressBar Example"

def example():
    from time import sleep

    t = ft.Text(value="Click the button...")
    pb = ft.ProgressBar(width=400, value=0)
    

    def button_clicked(e):
        t.value = "Doing something..."
        t.update()
        b.disabled = True
        b.update()
        for i in range(0, 101):
            pb.value = i * 0.01
            sleep(0.1)
            pb.update()
        t.value = "Click the button..."
        t.update()
        b.disabled = False
        b.update()

    b = ft.FilledTonalButton("Start", on_click=button_clicked)
    
    return ft.Column(
            [
                ft.Text("Linear progress indicator", style="headlineSmall"),
                ft.Column([t, pb]),
                ft.Text("Indeterminate progress bar", style="headlineSmall"),
                ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee"),
                b
            ],
            width=400,
            height=400
        )