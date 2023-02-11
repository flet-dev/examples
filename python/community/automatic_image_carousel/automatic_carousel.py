from flet import *
import time
import threading

class AutomaticImageCarousel(UserControl):
	def __init__(self, images_list, perseverance_time:float, animations:list, descriptive=True):
		super().__init__()
		self.descriptive = descriptive
		self.images_list = images_list
		self.perseverance_time = perseverance_time
		self.animation_in = animations[0]
		self.animation_out = animations[1]
		self.carousel = self.build_carousel()

	def did_mount(self):
		self.running = True
		self.th = threading.Thread(target=self.animate, args=(), daemon=True)
		self.th.start()

	def build_carousel(self):
		carousel = AnimatedSwitcher(
		        Column([], horizontal_alignment=CrossAxisAlignment.CENTER),
		        transition=AnimatedSwitcherTransition.FADE,
		        duration=500,
		        reverse_duration=500,
		        switch_in_curve=self.animation_in,
		        switch_out_curve=self.animation_out,
		    )
		return carousel

	def animate(self):
		ind = 0
		indexes = [Icon(icons.CIRCLE_OUTLINED,size=11) for _ in self.images_list]
		while True:
		    indexes[ind-1] = Icon(icons.CIRCLE_OUTLINED,size=11)
		    indexes[ind] = Icon(icons.CIRCLE_ROUNDED,size=15)
		    if self.descriptive == False:
		    	self.carousel.content = Column([
		        Container(
		                Image(src=self.images_list[ind][0],fit=ImageFit.FILL, border_radius=border_radius.all(5),),
		                border=border.all(1, colors.BLACK),
		                border_radius=border_radius.all(5),
		            ),
		        Row(indexes,alignment=MainAxisAlignment.CENTER),
		    ], horizontal_alignment=CrossAxisAlignment.CENTER,)
		    else:
			    self.carousel.content = Column([
			        Container(
			                Image(src=self.images_list[ind][0],fit=ImageFit.FILL, border_radius=border_radius.all(5),),
			                border=border.all(1, colors.BLACK),
			                border_radius=border_radius.all(5),
			            ),
			       	Text(self.images_list[ind][1]),
			        Row(indexes,alignment=MainAxisAlignment.CENTER),
			    ], horizontal_alignment=CrossAxisAlignment.CENTER,)
		    ind += 1
		    if ind == len(self.images_list):
		        ind = 0
		    self.update()
		    self.carousel.update()
		    time.sleep(self.perseverance_time)

	def build(self):
		return self.carousel