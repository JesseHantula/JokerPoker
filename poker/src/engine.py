from enum import Enum
from models import Deck, Player, Round

class GameState(Enum):
    PLAYING = 1
    BETTING = 2
    ENDING = 3

class Poker:
    def __init__(self):
        self.deck = Deck()
        self.round = Round()
        self.deck.shuffle()
        self.player1 = Player("jesse", 500)
        self.player2 = Player("james", 500)
        self.player3 = Player("josh", 500)
        self.player4 = Player("jake", 500)

        self.players = [self.player1, self.player2, self.player3, self.player4]
        self.current_player = self.player1
        self.state = GameState.PLAYING

    def switch_player(self):
        if self.current_player == self.player1:
            if self.player4.folded and self.player2.folded and self.player3.folded:
                self.state = GameState.ENDING
            elif self.player3.folded and self.player2.folded:
                self.current_player = self.player4
            elif self.player2.folded:
                self.current_player = self.player3
            else:
                self.current_player = self.player2
        elif self.current_player == self.player2:
            if self.player1.folded and self.player4.folded and self.player3.folded:
                self.state = GameState.ENDING
            elif self.player3.folded and self.player4.folded:
                self.current_player = self.player1
            elif self.player3.folded:
                self.current_player = self.player4
            else:
                self.current_player = self.player3
        elif self.current_player == self.player3:
            if self.player4.folded and self.player1.folded and self.player2.folded:
                self.state = GameState.ENDING
            elif self.player4.folded and self.player1.folded:
                self.current_player = self.player2
            elif self.player4.folded:
                self.current_player = self.player1
            else:
                self.current_player = self.player4
        elif self.current_player == self.player4:
            if self.player1.folded and self.player2.folded and self.player3.folded:
                self.state = GameState.ENDING
            elif self.player1.folded and self.player2.folded:
                self.current_player = self.player3
            elif self.player1.folded:
                self.current_player = self.player2
            else:
                self.current_player = self.player1

    def play(self, key):
        if key is None:
            return

        if self.state == GameState.ENDING:
            return

        if key == self.current_player.raise_key:
            self.current_player.make_bet += 50
            self.round.pot += 50
            self.current_player.money -= 50
            self.switch_player()
            return

        if key == self.current_player.call_key:
            self.current_player.make_bet += 50
            self.round.pot += 50
            self.current_player.money -= 50
            self.switch_player()
            return

        if key == self.current_player.fold_key:
            self.current_player.discard_all()
            self.switch_player()
            return
