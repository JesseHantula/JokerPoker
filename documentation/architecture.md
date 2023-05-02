# Architectural description
## Structure
##### The structure of the project follows the architecture shown below:
![Diagram](./pictures/architecture.png)

## Application logic
The following diagram shows the flow of the application logic:
```mermaid
    sequenceDiagram
        participant User
        participant Game
        User->>Game: Initialize Game
        activate Game
        Game-->>User: Game window displayed
        User->>Game: Click Start button
        Game->>Poker: Initialize Poker game
        activate Poker
        Poker->>Deck: Initialize Deck of cards
        Deck-->>Poker: Deck of cards created
        Poker->>Game: Start the game
        Game->>Poker: Deal initial hand
        Poker->>Game: Show the initial hand
        Game-->>User: Show the initial hand of cards
        User->>Game: Select cards to hold
        Game->>Poker: Set held cards and deal new cards
        Poker->>Game: Show the new hand
        Game->>Poker: Determine winner of the game
        Poker-->>Game: Display winner of the game
        Game-->>User: Show the new hand of cards and results of the game
        User->>Game: Click 'Start' button to play again
        deactivate Poker
        deactivate Game
```