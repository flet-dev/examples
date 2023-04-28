import flet as ft

name = "Font with variable weight"

def example():

    class Example(ft.Column):
        def __init__(self):
            super().__init__()
            self.t = ft.Text(
                "This is rendered with Roboto Slab",
                size=30,
                font_family="RobotoSlab",
                weight=ft.FontWeight.W_100,)
            self.controls = [
                self.t,
                ft.Slider(
                    min=100,
                    max=900,
                    divisions=8,
                    label="{value}",
                    width=500,
                    on_change=self.width_changed,
                ),
                ]

        # happens when example is added to the page (when user chooses the Text control from the grid)
        def did_mount(self):
            self.page.fonts["RobotoSlab"] = "RobotoSlab[wght].ttf"
            self.page.update()
        
        def width_changed(self, e):
            self.t.weight = f"w{int(e.control.value)}"
            self.t.update()

    
    example = Example()
    
    return example


# import flet as ft

# name = "Autoplay Audio"

# def example():
#     class Example(ft.Column):
#         def __init__(self):
#             super().__init__()
#             self.audio1 = ft.Audio(
#                 src="https://luan.xyz/files/audio/ambient_c_motion.mp3", autoplay=True)
            
#             self.controls = [ft.Text("This is an app with background audio. Note: this example doesn't work in Safari browser."),
#         ft.ElevatedButton("Stop playing", on_click=lambda _: self.audio1.pause())]
            

#         # happens when example is added to the page (when user chooses the Audio control from the grid)
#         def did_mount(self):
#             self.page.overlay.append(self.audio1)
#             self.page.update()
        
#         # happens when example is removed from the page (when user chooses different control group on the navigation rail)
#         def will_unmount(self):
#             self.page.overlay.remove(self.audio1)
#             self.page.update()
  
#     audio_example = Example()
    
#     return audio_example