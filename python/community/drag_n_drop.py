import flet as ft
import flet.canvas as cv 
import random

class State:
    x: float
    y: float


state = State()


colors_list =[ 
ft.colors.BLACK12 ,
ft.colors.GREEN_100 ,
ft.colors.BLACK38 ,
ft.colors.GREEN_200 ,
ft.colors.BLACK54 ,
ft.colors.GREEN_50 ,
ft.colors.BLACK   ,
ft.colors.RED     ,
ft.colors.RED_50  ,
ft.colors.RED_100 ,
ft.colors.RED_200 ,
ft.colors.RED_300 ,
ft.colors.GREEN ,
ft.colors.GREEN_200 ,
ft.colors.GREEN_300 ,
ft.colors.RED_700 ,
ft.colors.RED_800 ,
ft.colors.RED_900 ,
ft.colors.PINK ,
ft.colors.PINK_50 ,
ft.colors.PINK_100 ,
ft.colors.PINK_200 ,
ft.colors.PINK_300 ,
ft.colors.PINK_400 ,
ft.colors.LIGHT_BLUE_100 ,
ft.colors.PINK_600 ,
ft.colors.AMBER ,
ft.colors.LIGHT_BLUE_ACCENT ,
ft.colors.PINK_900 ,
ft.colors.PURPLE   ,
ft.colors.GREY ,
ft.colors.PURPLE_100 ,
ft.colors.PURPLE_200 ,
ft.colors.YELLOW ,
ft.colors.PURPLE_400 ,
ft.colors.GREEN ,
ft.colors.PURPLE_600 ,
ft.colors.PURPLE_700 ,
ft.colors.PURPLE_800 ,
ft.colors.DEEP_ORANGE ,
ft.colors.DEEP_PURPLE ,
ft.colors.DEEP_PURPLE_50 ,
ft.colors.DEEP_PURPLE_100 ,
ft.colors.DEEP_PURPLE_200 ,
ft.colors.DEEP_PURPLE_300 ,
ft.colors.DEEP_PURPLE_400 ,
ft.colors.DEEP_PURPLE_500 ,
ft.colors.AMBER ,
ft.colors.DEEP_PURPLE_700 ,
ft.colors.DEEP_PURPLE_800 ,
ft.colors.DEEP_PURPLE_900 ]



def main(page: ft.Page):
    page.title = "ft cube test"
    message = "Arrastra los cubos doble click el editar texto 1 2 3 4 5 6 7 8 9 0"
     
    rects = []
    hearths = []
    texts = []

    


    def Start_draging(e: ft.DragStartEvent):
        state.x = e.local_x
        state.y = e.local_y
        print("Start")
    def move(e: ft.DragUpdateEvent):

        #print(cp.shapes) 

        state.x = e.local_x
        state.y = e.local_y

        for i,rect in enumerate(rects):
          
            if(
                e.local_x >= rect.x   
                and e.local_x <=  rect.x +rect.width 
                and e.local_y >= rect.y   
                and e.local_y <= rect.y +rect.height 
                ):

                rect.x = state.x - (rect.width/2)
                rect.y = state.y- (rect.height/2)
                texts[i].x, texts[i].y = state.x- (rect.width/2) , state.y - (rect.height/2)  
                break

        #print(hearths[0].elements)
        #print("Move")
        #print(hearths)
        cp.update()

    def start_edit_text(e: ft.MultiTapEvent):
        
        print("entro")
        print("data", e)
        for i,rect in enumerate(rects):
            if(
                state.x >= rect.x   
                and state.x <=  rect.x +rect.width 
                and state.y >= rect.y   
                and state.y <= rect.y +rect.height 
                ):
                print("Encontro")
                texts[i].text = ""
                break

    def create_rects():
        for i in range(random.randint(8,13)):

            
            x_r = random.randint(10,500)
            y_r = random.randint(10,500)
            lado =random.randint(15,150) 
            
            if(True):
                rect = cv.Rect(
                    
                    x_r,
                    y_r,
                    lado ,
                    lado ,
                    
                    
                    paint=ft.Paint(style=ft.PaintingStyle.FILL, 
                                color=random.choice(colors_list)))
                
                text = cv.Text(x_r,y_r,text=message.split(" ")[i%len(message.split(" "))],style=ft.TextStyle(lado/2, decoration_color=random.choice(colors_list)))
                rects.append(rect)
                texts.append(text)
                print("Se agrego un rect")
                cp.shapes.append(rect)
                cp.shapes.append(text)
            else:
                hearth = cv.Path(
                [
                    cv.Path.SubPath(
                        [
                            cv.Path.MoveTo(75, 40),
                            cv.Path.CubicTo(75, 37, 70, 25, 50, 25),
                            cv.Path.CubicTo(20, 25, 20, 62.5, 20, 62.5),
                            cv.Path.CubicTo(20, 80, 40, 102, 75, 120),
                            cv.Path.CubicTo(110, 102, 130, 80, 130, 62.5),
                            cv.Path.CubicTo(130, 62.5, 130, 25, 100, 25),
                            cv.Path.CubicTo(85, 25, 75, 37, 75, 40),
                        ],
                        random.randint(10,600),
                        random.randint(10,600),
                    )
                ],
                paint=ft.Paint(
                    gradient=ft.PaintRadialGradient(
                        ft.Offset(150, 150), 50, [ft.colors.PINK, ft.colors.PINK_ACCENT]
                    ),
                    style=ft.PaintingStyle.FILL,
                ))
                print("Se agrego un cora")
                hearths.append(hearth)
                cp.shapes.append(hearth)
        cp.update()

    cp = cv.Canvas(
        [

           cv.Fill(
               ft.Paint(
                   gradient=ft.PaintLinearGradient(
                       (0,0), (500,400), colors=[ft.colors.AMBER, ft.colors.PINK]
                   )
               )
           )
        ], 
        content= ft.GestureDetector(
            on_pan_start=Start_draging,
            on_pan_update=move,
            on_double_tap=start_edit_text,
            drag_interval=5,
        ),
        expand=False
    ) 
    

    page.add(
        ft.Container(
            cp,
            border_radius=5,
            width=float("inf"),
            expand=True,
        )
    )
    create_rects()


ft.app(main)
