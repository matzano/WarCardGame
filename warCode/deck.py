from cards import Card
from random import shuffle
class Deck:
    def __init__(self):
        self.fullDeck = []


    def create_deck(self):
        for i in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for j in range(1,14):
                self.fullDeck.append(Card(i,j))
        shuffle(self.fullDeck)

    

    def pull_card(self):
        if len(self.fullDeck) == 0:
            return
        return self.fullDeck.pop()
        

#game = Deck()
#game.create_deck()
#card = game.pull_card()
#card.show_Card()

