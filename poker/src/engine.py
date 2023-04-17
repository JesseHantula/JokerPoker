from enum import Enum
import pygame
from models import *

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
        self.player2, self.player3, self.player4 = Bot("bot1", 500), Bot("bot2", 500), Bot("bot3", 500)
        self.players = [self.player1, self.player2, self.player3, self.player4]
        self.currentPlayer = self.player1
        self.state = GameState.PLAYING
        
    def switchPlayer(self):
        if self.currentPlayer == self.player1:
            if self.player4.folded and self.player2.folded and self.player3.folded:
                self.state = GameState.ENDING
            elif self.player3.folded and self.player2.folded:
                self.currentPlayer = self.player4
            elif self.player2.folded:
                self.currentPlayer = self.player3
            else:
                self.currentPlayer = self.player2
        elif self.currentPlayer == self.player2:
            if self.player1.folded and self.player4.folded and self.player3.folded:
                self.state = GameState.ENDING
            elif self.player3.folded and self.player4.folded:
                self.currentPlayer = self.player1
            elif self.player3.folded:
                self.currentPlayer = self.player4
            else:
                self.currentPlayer = self.player3
        elif self.currentPlayer == self.player3:
            if self.player4.folded and self.player1.folded and self.player2.folded:
                self.state = GameState.ENDING
            elif self.player4.folded and self.player1.folded:
                self.currentPlayer = self.player2
            elif self.player4.folded:
                self.currentPlayer = self.player1
            else:
                self.currentPlayer = self.player4
        elif self.currentPlayer == self.player4:
            if self.player1.folded and self.player2.folded and self.player3.folded:
                self.state = GameState.ENDING
            elif self.player1.folded and self.player2.folded:
                self.currentPlayer = self.player3
            elif self.player1.folded:
                self.currentPlayer = self.player2
            else:
                self.currentPlayer = self.player1

    def play(self, key):
        if key == None:
            return
        
        if self.state == GameState.ENDING:
            return
        
        if key == self.currentPlayer.raiseKey:
            self.currentPlayer.bet += 50
            self.pot += 50
            self.currentPlayer.money -= 50
            self.switchPlayer()
            return
        
        if key == self.currentPlayer.callKey:
            self.currentPlayer.bet += 50
            self.pot += 50
            self.currentPlayer.money -= 50
            self.switchPlayer()
            return
        
        if key == self.currentPlayer.foldKey:
            self.currentPlayer.discardAll()
            self.switchPlayer()
            return