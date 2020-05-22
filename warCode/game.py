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
        return theDeck
        



    def game_procedure(self):
        gameDeck = self.deck_for_game()
        lenofGameDeck = len(gameDeck.fullDeck)
        player1 = self.players[0]
        count = 0
        
        while lenofGameDeck >= 26:
            card = gameDeck.pull_card()
            player1.cards.append(card)
            lenofGameDeck -= 1
        while lenofGameDeck > 0:
            card = gameDeck.pull_card()
            self.computer.cards.append(card)
            lenofGameDeck -= 1

    
        while len(player1.cards) > 0 and len(self.computer.cards) > 0:
            p1Card = player1.pull_card()
            compCard = self.computer.pull_card()
            if p1Card.value > compCard.value:
                player1.win += 1
            else:
                self.computer.win += 1

        print("{} Wins: {}".format(player1.name, player1.win))
        print("Computer Wins: {}".format(self.computer.win))
        if player1.win > self.computer.win:
            print("{} Wins Game! ".format(player1.name))
        else:
            print("Computer Wins!")
        
        print("------------------------")
        print("Game Over!")
    



game = Game()
game.add_player("Joe")
game.game_procedure()