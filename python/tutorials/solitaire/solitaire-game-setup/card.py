CARD_WIDTH = 70
CARD_HEIGTH = 100
DROP_PROXIMITY = 30
CARD_OFFSET = 20

import flet as ft

class Card(ft.GestureDetector):
    def __init__(self, solitaire, suite, rank):
        super().__init__()
        self.mouse_cursor=ft.MouseCursor.MOVE
        self.drag_interval=5
        self.on_pan_start=self.start_drag
        self.on_pan_update=self.drag
        self.on_pan_end=self.drop
        self.suite=suite
        self.rank=rank
        self.face_up=False
        self.top=None
        self.left=None
        self.solitaire = solitaire
        self.slot = None
        self.content=ft.Container(
            width=CARD_WIDTH, 
            height=CARD_HEIGTH, 
            border_radius = ft.border_radius.all(6), 
            content=ft.Image(src="card_back.png"))

    def turn_face_up(self):
        """Reveals card"""
        self.face_up = True
        self.content.content.src=f"/images/{self.rank.name}_{self.suite.name}.svg"
        self.update()

    def move_on_top(self):
        """Brings draggable card pile to the top of the stack"""

        for card in self.get_draggable_pile():
            self.solitaire.controls.remove(card)
            self.solitaire.controls.append(card)
        self.solitaire.update()

    def bounce_back(self):
        """Returns draggable pile to its original position"""
        draggable_pile = self.get_draggable_pile()
        for card in draggable_pile:
            if card.slot in self.solitaire.tableau:
                card.top = card.slot.top + card.slot.pile.index(card) * CARD_OFFSET
            else:
                card.top = card.slot.top
            card.left = card.slot.left
        self.solitaire.update()

    def place(self, slot):
        """Place draggable pile to the slot"""
        
        draggable_pile = self.get_draggable_pile()

        for card in draggable_pile:
            if slot in self.solitaire.tableau:
                card.top = slot.top + len(slot.pile) * CARD_OFFSET
            else:
                card.top = slot.top
            card.left = slot.left

            # remove card from it's original slot, if exists
            if card.slot is not None:
                card.slot.pile.remove(card)
        
            # change card's slot to a new slot
            card.slot = slot

            # add card to the new slot's pile
            slot.pile.append(card)
        
        self.solitaire.update()

    def get_draggable_pile(self):
        """returns list of cards that will be dragged together, starting with the current card"""
        if self.slot is not None:
            return self.slot.pile[self.slot.pile.index(self):]
        return [self]

    def start_drag(self, e: ft.DragStartEvent):
        self.move_on_top()
        self.update()

    
    def drag(self, e: ft.DragUpdateEvent):
        draggable_pile = self.get_draggable_pile()
        for card in draggable_pile:
            card.top = max(0, self.top + e.delta_y) + draggable_pile.index(card) * CARD_OFFSET
            card.left = max(0, self.left + e.delta_x)
            card.update()


    def drop(self, e: ft.DragEndEvent):
        for slot in self.solitaire.tableau:
            if (
                abs(self.top - (slot.top + len(slot.pile) * CARD_OFFSET)) < DROP_PROXIMITY
            and abs(self.left - slot.left) < DROP_PROXIMITY
          ):
                self.place(slot)
                self.update()
                return
        for slot in self.solitaire.foundations:
            if (
                abs(self.top - slot.top) < DROP_PROXIMITY
            and abs(self.left - slot.left) < DROP_PROXIMITY
          ):
                self.place(slot)
                self.update()
                return
           
        self.bounce_back()
        self.update()