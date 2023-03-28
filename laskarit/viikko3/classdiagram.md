```mermaid
classDiagram
    Board --> "2-8" Player
      class Player{
          player_piece
          password
      }
      class Board{
          square
          dice
          player
      }
```