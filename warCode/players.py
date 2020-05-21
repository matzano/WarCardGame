class Player:
    def __init__(self, name):
        self.name = name
        self.win = 0
        self.cards = []

    def pull_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
        
        


