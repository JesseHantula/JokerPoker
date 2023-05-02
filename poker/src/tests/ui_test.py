import unittest
from ui.game_ui import Game


class TestGame(unittest.TestCase):
    def test_start(self):
        game = Game()
        self.assertEqual(game.scoreboard, [0,0,0,0])
        self.assertEqual(game.state, 0)
        
    def test_play(self):
        game = Game()
        game.play_init()
        game.play()
        
        