from deck import Deck
from players import Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.computer = Player("Computer")
        self.players = []
    
    def add_player(self, name):
        player = Player(name)
        self.players.append(player)

    def deck_for_game(self):
        theDeck = Deck()
        theDeck.create_deck()
        myDeck = theDeck.fullDeck
        return myDeck



    def game_procedure(self):
        gameDeck = self.deck_for_game()
        player1 = self.players[0]
        count = 0
        for card in gameDeck:
            player1.cards.append(card)
            count += 1
            if count > 26:
                break
        for card in gameDeck:
            self.computer.cards.append(card)

        player1CardLen = len(player1.cards)
        compCardLen = len(self.computer.cards)
    
        while player1CardLen > 0 and compCardLen > 0:
            p1Card = player1.pull_card()
            compCard = self.computer.pull_card()
            if p1Card.value > compCard.value:
                playerWins = player1.win
                playerWins += 1
            else:
                computerWins = compCard.win
                computerWins += 1

            
        
        
    



game = Game()
game.add_player("matt")
game.game_procedure()