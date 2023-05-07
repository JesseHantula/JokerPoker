from entities.models import Deck

class Poker:
    """Poker game engine
    Attributes: scores (list): list of scores for each player"""
    def __init__(self, scores):
        """Initializes poker game engine"""
        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = self.deck.deal()
        self.bot1_hand = self.deck.deal()
        self.bot2_hand = self.deck.deal()
        self.bot3_hand = self.deck.deal()

        self.scores = scores
        self.cards_to_replace = []

    def replace_cards(self, cards_to_replace):
        """Replace cards in player's hand with new cards from deck
        Args: cards_to_replace (list): list of cards to replace
        """ 
        for card in cards_to_replace:
            self.player_hand.remove(card)
            self.player_hand.append(self.deck.draw())
            
    def convert(self, winner):
        """Convert score to a string
        Args: score (int): score of the hand
        Returns: string of the score
        """
        ret = []
        if winner[0] == 0:
            ret.append("You")
        elif winner[0] == 1:
            ret.append("Bot 1")
        elif winner[0] == 2:
            ret.append("Bot 2")
        elif winner[0] == 3:
            ret.append("Bot 3")

        if int(winner[1]) == 0:
            ret.append("High Card")
        elif int(winner[1]) == 1:
            ret.append("Pair")
        elif int(winner[1]) == 2:
            ret.append("Two Pair")
        elif int(winner[1]) == 3:
            ret.append("Three of a Kind")
        elif int(winner[1]) == 4:
            ret.append("Straight")
        elif int(winner[1]) == 5:
            ret.append("Flush")
        elif int(winner[1]) == 6:
            ret.append("Full House")
        elif int(winner[1]) == 7:
            ret.append("Four of a Kind")
        elif int(winner[1]) == 8:
            ret.append("Straight Flush")
        elif int(winner[1]) == 9:
            ret.append("Royal Flush")
        return ret
             
    def check_hand(self, hand):
        """Check hand and give it a score based on the cards in the hand
        Args: hand (list): list of cards in hand
        Returns: score (int): score of the hand, ranges from 0 (high card) to 9 (royal flush)
        """
        score = 0
        #convert the hand to a list of tuples (suit, value)
        hand_values = []
        for card in hand:
            hand_values.append((card.suit, card.value))
        #sort the hand by value
        hand_values.sort(key=lambda x: x[1])
        #check for royal flush
        if self.check_royal_flush(hand_values):
            score = 9
        elif self.check_straight_flush(hand_values):
            score = 8
            score += hand_values[4][1] / 100
        elif self.check_four_of_a_kind(hand_values):
            score = 7
            if hand_values[2][1] == 1:
                score += 14/100
            else:
                score += hand_values[2][1] / 100       
        elif self.check_full_house(hand_values):
            score = 6
            if hand_values[1][1] == 1:
                score += 14/100
            else:
                score += hand_values[3][1] / 100    
        elif self.check_flush(hand_values):
            score = 5
            if hand_values[0][1] == 1:
                score += 13/100
            else:
                score += hand_values[4][1] / 100    
        elif self.check_straight(hand_values):
            score = 4
            if hand_values[0][1] == 1:
                score += 14/100
            else:
                score += hand_values[4][1] / 100
        elif self.check_three_of_a_kind(hand_values):
            score = 3
            if hand_values[2][1] == 1:
                score += 14/100
            else:
                score += hand_values[2][1] / 100
        elif self.check_two_pair(hand_values):
            score = 2
            if hand_values[1][1] == 1:
                score += 14/100
            else:
                score += hand_values[3][1] / 100
        elif self.check_pair(hand_values)[0] == True:
            score = 1
            index = self.check_pair(hand_values)[1]
            if hand_values[index][1] == 1:
                score += 14/100
            else:
                score += hand_values[index][1] / 100
        else:
            if hand_values[0][1] == 1:
                score += 14/100
            else:
                score += hand_values[4][1] / 100
        return score

    def check_royal_flush(self, hand):
        """Check if hand is a royal flush
        Args: hand (list): list of cards in hand
        Returns: True if hand is a royal flush, False otherwise
        """
        if self.check_flush(hand) and hand[0][1] == 1:
            if hand[1][1] == 10 and hand[2][1] == 11 and hand[3][1] == 12 and hand[4][1] == 13:
                return True
        return False

    def check_straight_flush(self, hand):
        """Check if hand is a straight flush
        Args: hand (list): list of cards in hand
        Returns: True if hand is a straight flush, False otherwise
        """
        if self.check_flush(hand) and self.check_straight(hand):
            return True
        return False

    def check_four_of_a_kind(self, hand):
        """Check if hand is a four of a kind
        Args: hand (list): list of cards in hand
        Returns: True if hand is a four of a kind, False otherwise
        """
        for i in range(len(hand) - 3):
            if hand[i][1] == hand[i+1][1] == hand[i+2][1] == hand[i+3][1]:
                return True
        return False

    def check_full_house(self, hand):
        """Check if hand is a full house
        Args: hand (list): list of cards in hand
        Returns: True if hand is a full house, False otherwise
        """
        if hand[0][1] == hand[1][1] == hand[2][1] and hand[3][1] == hand[4][1]:
            return True
        if hand[0][1] == hand[1][1] and hand[2][1] == hand[3][1] == hand[4][1]:
            return True
        return False

    def check_flush(self, hand):
        """Check if hand is a flush
        Args: hand (list): list of cards in hand
        Returns: True if hand is a flush, False otherwise
        """
        for i in range(len(hand) - 1):
            if hand[i][0] != hand[i+1][0]:
                return False
        return True

    def check_straight(self, hand):
        """Check if hand is a straight
        Args: hand (list): list of cards in hand
        Returns: True if hand is a straight, False otherwise
        """
        for i in range(len(hand) - 1):
            if hand[i][1] + 1 != hand[i+1][1]:
                return False
        return True

    def check_three_of_a_kind(self, hand):
        """Check if hand is a three of a kind
        Args: hand (list): list of cards in hand
        Returns: True if hand is a three of a kind, False otherwise
        """
        for i in range(len(hand) - 2):
            if hand[i][1] == hand[i+1][1] == hand[i+2][1]:
                return True
        return False

    def check_two_pair(self, hand):
        """Check if hand is a two pair
        Args: hand (list): list of cards in hand
        Returns: True if hand is a two pair, False otherwise
        """
        if hand[0][1] == hand[1][1] and hand[2][1] == hand[3][1]:
            return True
        if hand[0][1] == hand[1][1] and hand[3][1] == hand[4][1]:
            return True
        if hand[1][1] == hand[2][1] and hand[3][1] == hand[4][1]:
            return True
        return False

    def check_pair(self, hand):
        """Check if hand is a pair
        Args: hand (list): list of cards in hand
        Returns: True if hand is a pair, False otherwise
        """
        for i in range(len(hand) - 1):
            if hand[i][1] == hand[i+1][1]:
                return (True, i)
        return (False, i)
    
    def get_winner(self):
        scores = []
        scores.append(self.check_hand(self.player_hand))
        scores.append(self.check_hand(self.bot1_hand))
        scores.append(self.check_hand(self.bot2_hand))
        scores.append(self.check_hand(self.bot3_hand))

        winner = 0
        score = scores[0]
        for i in range(1, 4):
            if scores[i] > scores[winner]:
                winner = i
                score = scores[i]
            
        return winner, score


