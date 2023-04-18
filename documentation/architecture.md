```mermaid
graph TD
    A[Main] --> B[Engine]
    A --> C[Models]
    B --> C
    C["Models (contains objects)"]
    B["Engine (contains game object)"]
    A["Main (contains game logic)"]
```