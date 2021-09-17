import random

class Card:
    def __init__(self, suit, val, name):
        self.suit = suit
        self.val = val
        self.name = name

    def show_card(self):
        if self.val > 9:
            print(
f'''
+--------+
|{self.val}      |
|        |
|        |
|        |
|      {self.val}|
+--------+
{self.suit}
''')
        else:
            print(
f'''
+--------+
|{self.val}       |
|        |
|        |
|        |
|       {self.val}|
+--------+
{self.suit}
''')

    def __repr__(self):
        return f'{self.name}({self.val}) of {self.suit}'

class Deck:
    game_cards = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five':5,
                'Six': 6, 'Seven': 7, 'Jack':10, 'Queen': 11, 'King':12}

    suit_type = ['<(-_|_-)>', 'O===--*', '[$$$]', '+|===>']

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in self.suit_type:
            for key, value in self.game_cards.items():
                self.cards.append(Card(suit, value, key))
        random.shuffle(self.cards)

    # shows all card in deck
    def show(self):
        for c in self.cards:
            c.show_card()

    def draw_card(self):
        # if no cards left in current deck, rebuild and shuffle.
        if self.cards == []:
            self.build()
            random.shuffle(self.cards)
        return self.cards.pop()