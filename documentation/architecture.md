# Architectural description
## Structure
The structure of the project follows the architecture shown below:

![Diagram](./pictures/architecture.png)

## User Interface
There are 3 main windows in the application:
* Starting screen
* Game screen
* Ending screen

From the start screen, the user can start the game and will be brought to the game screen. From the game screen, the user can play the game and will be brought to the results screen. From the results screen, the user can start the game again and will be brought to the game screen.

## Application Logic
The main logical aspect of this project is used to calculate a winner. This is done by comparing the hands of each player, and determining which hand is the best. The hands are compared by first checking the hand ranking, and then checking the high card. If the hand ranking is the same, then the high card is used to determine the winner. 
```mermaid
classDiagram
    Round --> Winner
    class Round{
        players
    }
    class Winner{
        hand ranking
        high card
        player
    }
```
## Main Functions
### Starting a game
The following diagram shows the flow of the game logic:
```mermaid
    sequenceDiagram
        User->>Game: Initialize Game
        activate Game
        Game-->>User: Game window displayed
        User->>Game: Click Start button
        Game->>Poker: Initialize Poker game
        activate Poker
        Poker->>Deck: Initialize Deck of cards
        Deck-->>Poker: Deck of cards created
        Poker-->>Game: Start the game
        Game->>Poker: Deal initial hand
        Poker-->>Game: Show the initial hand
        Game-->>User: Show the initial hand of cards
        User->>Game: Select cards to hold
        Game->>Poker: Set held cards and deal new cards
        Poker-->>Game: Show the new hand
        Game->>Poker: Determine winner of the game
        Poker-->>Game: Display winner of the game
        Game-->>User: Show the new hand of cards and results of the game
        User->>Game: Click 'Start' button to play again
```

Once a player starts up the game, the game window is displayed. The player can then click the 'Start' button to start the game. The game is initialized, and the initial hand is dealt. The player can then select which cards to hold, and the new cards are dealt. The winner of the game is then determined, and the results are displayed. The player can then click the 'Start' button to play again.