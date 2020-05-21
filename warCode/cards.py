class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.card = None
        
    def show_Card(self):
        print( '{} of {}' .format(self.value, self.suit))



        




