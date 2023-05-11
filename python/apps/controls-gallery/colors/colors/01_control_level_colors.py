import flet as ft

name = "Color property defined on a control level"

def example():
    import re
    
    def change_bgcolor_A(e):
        #match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', textfield_A.value)

        #if match:                      
        button_A.bgcolor = textfield_A.value
        textfield_A.value = ""
        textfield_A.error_text = ""
        #else:
        #    textfield_A.error_text = "Hex value is not valid"
        #if textfield_A.value[:2] == "ft":
        # try:
        #     
        # except:            
        #     print("Nice try!")
        
        button_A.update()
        textfield_A.update()
    
    button_A = ft.ElevatedButton(text="Elevated Button A")
    textfield_A = ft.TextField(label="Hex value in format #AARRGGBB or #RRGGBB")
    return ft.Column(controls=[
        button_A,
        ft.ElevatedButton("Elevated Button B"),
        ft.Row(controls=[
            textfield_A,
            ft.FilledButton(text="Change Elevated Button A bgcolor", on_click=change_bgcolor_A)
        ])
    ])