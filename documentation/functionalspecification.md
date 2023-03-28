# Functional specification
## General Overview
##### This project contains a version of the card game known as Poker. This project follows the rules of the "Texas hold 'em" version of poker, which involves each player getting 2 cards, and 5 community cards are dealt in various turns. The player that has the best "hand" wins the round, and receives all the money that was put in by each player in the round. The "hand" rankings are as follows:
##### 1. Royal flush
##### 2. Straight flush
##### 3. Four of a kind
##### 4. Full house
##### 5. Flush
##### 6. Straight
##### 7. Three of a kind
##### 8. Two pairs
##### 9. Pair
##### 10. High card
##### In the case of a tie (ie. two players have a three of a kind), the player with the higher card wins (ie. a player with three 10's beats a player with three 5's).

## Players
##### There is only a one-player mode for this game, where the player plays against 3 bots.

## Designed Functionalities
#### Apply the following game structure:
* Each player starts with two random cards from the deck, making sure that no player has the same card as another player.
* Each player starts with $250. 
* Each player takes turns putting down money for the round, each player must put in at least $10 (ante). The player can also drop out (fold) instead of placing down money. Also, each player must have put in the same amount of money (for example, if one player puts down $100, each player must match that amount or drop out). 
* The dealer places down three cards, all of which can be seen by each player.
* The players again take turns raising the amount of money, or calling (not raising the money).
* The dealer places down a fourth card, and the process repeats.
* The dealer places down a fifth and final card, and the players again either raise or call.
* Once the players are done raising money, they show their cards and reveal the winner.
* The winner of the round receives all the money put in from the players, and the next round is played.
* The game continues until either all players except for one run out of money, or if the player quits.
* A winner screen is presented, with an option to play again or quit.

## Additional Functionality Ideas
* Create a "party mode", where multiple players can take turns playing on the same device.
* Change the amount of bots the user can play against.
* Make multiple options for starting amount of cash, and ante.
* Create multiple difficulties for the bots, such that the hardest difficulty bots will make smarter decisions, whereas the easier difficulty bots will often make mistakes.
* Create a leaderboard system such that players can keep track of their wins (this would also require a login system in most cases). 
