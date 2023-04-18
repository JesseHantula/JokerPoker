```mermaid
graph TD
    A[main] --> B[engine]
    A --> C[models]
    B --> C
    C["models contains objects"]
    B["engine contains game object"]
    A["main contains game logic"]
```