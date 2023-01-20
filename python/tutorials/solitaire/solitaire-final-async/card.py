import flet as ft

CARD_WIDTH = 70
CARD_HEIGTH = 100
DROP_PROXIMITY = 30
CARD_OFFSET = 20


class Card(ft.GestureDetector):
    def __init__(self, solitaire, suite, rank):
        super().__init__()
        self.mouse_cursor = ft.MouseCursor.MOVE
        self.drag_interval = 5
        self.on_pan_start = self.start_drag
        self.on_pan_update = self.drag
        self.on_pan_end = self.drop
        self.on_tap = self.click
        self.on_double_tap = self.doubleclick
        self.suite = suite
        self.rank = rank
        self.face_up = False
        self.top = None
        self.left = None
        self.solitaire = solitaire
        self.slot = None
        self.content = ft.Container(
            width=CARD_WIDTH,
            height=CARD_HEIGTH,
            border_radius=ft.border_radius.all(6),
            content=ft.Image(src="/images/card_back.png"),
        )

    async def turn_face_up(self):
        """Reveals card"""
        self.face_up = True
        self.content.content.src = f"/images/{self.rank.name}_{self.suite.name}.svg"
        await self.update_async()

    async def turn_face_down(self):
        """Hides card"""
        self.face_up = False
        self.content.content.src = "/images/card_back.png"
        await self.update_async()

    async def move_on_top(self):
        """Brings draggable card pile to the top of the stack"""

        for card in self.get_draggable_pile():
            self.solitaire.controls.remove(card)
            self.solitaire.controls.append(card)
        await self.solitaire.update_async()

    async def bounce_back(self):
        """Returns draggable pile to its original position"""
        draggable_pile = self.get_draggable_pile()
        for card in draggable_pile:
            if card.slot in self.solitaire.tableau:
                card.top = card.slot.top + card.slot.pile.index(card) * CARD_OFFSET
            else:
                card.top = card.slot.top
            card.left = card.slot.left
        await self.solitaire.update_async()

    async def place(self, slot):
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

        if self.solitaire.check_win():
            await self.solitaire.winning_sequence()

        await self.solitaire.update_async()

    def get_draggable_pile(self):
        """returns list of cards that will be dragged together, starting with the current card"""
        if (
            self.slot is not None
            and self.slot != self.solitaire.stock
            and self.slot != self.solitaire.waste
        ):
            return self.slot.pile[self.slot.pile.index(self) :]
        return [self]

    async def start_drag(self, e: ft.DragStartEvent):
        if self.face_up:
            await self.move_on_top()
            await self.update_async()

    async def drag(self, e: ft.DragUpdateEvent):
        if self.face_up:
            draggable_pile = self.get_draggable_pile()
            for card in draggable_pile:
                card.top = (
                    max(0, self.top + e.delta_y)
                    + draggable_pile.index(card) * CARD_OFFSET
                )
                card.left = max(0, self.left + e.delta_x)
                await card.update_async()

    async def drop(self, e: ft.DragEndEvent):
        if self.face_up:
            for slot in self.solitaire.tableau:
                if (
                    abs(self.top - (slot.top + len(slot.pile) * CARD_OFFSET))
                    < DROP_PROXIMITY
                    and abs(self.left - slot.left) < DROP_PROXIMITY
                ) and self.solitaire.check_tableau_rules(self, slot):
                    await self.place(slot)
                    await self.update_async()
                    return

            if len(self.get_draggable_pile()) == 1:
                for slot in self.solitaire.foundations:
                    if (
                        abs(self.top - slot.top) < DROP_PROXIMITY
                        and abs(self.left - slot.left) < DROP_PROXIMITY
                    ) and self.solitaire.check_foundations_rules(self, slot):
                        await self.place(slot)
                        await self.update_async()
                        return

            await self.bounce_back()
            await self.update_async()

    async def click(self, e):
        if self.slot in self.solitaire.tableau:
            if not self.face_up and self == self.slot.get_top_card():
                await self.turn_face_up()
                await self.update_async()
        elif self.slot == self.solitaire.stock:
            await self.move_on_top()
            await self.place(self.solitaire.waste)
            await self.turn_face_up()
            await self.solitaire.update_async()

    async def doubleclick(self, e):
        if self.face_up:
            await self.move_on_top()
            for slot in self.solitaire.foundations:
                if self.solitaire.check_foundations_rules(self, slot):
                    await self.place(slot)
                    await self.page.update_async()
                    return
