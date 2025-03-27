# **2048 Classical AI**  

## **Introduction**  

I've always been fascinated by **Artificial Intelligence**, especially in the realm of games. During my undergraduate years, I spent countless hours watching AI agents being trained to play games like *Mortal Kombat* and *Street Fighter*. In my senior year, I took my first **AI course**, where I was introduced to the **Minimax algorithm**—a decision-making approach using **recursion** and **backtracking** to solve game theory problems.  

While I understood the algorithm’s theoretical applications, I lacked hands-on experience with implementing it or truly grasping its high-level mechanics. I could manually construct a **Minimax decision tree**, but that was the extent of my knowledge.  

This project provided an opportunity to **deepen my understanding** by implementing Minimax in a game with a reasonably sized **search space**: **2048**.  

---  

## **Background**  

### **Understanding 2048**  

2048 is a **sliding tile puzzle game** where players merge tiles to form a **2048 tile**. The game begins with **two tiles** (either 2 or 4), and players slide tiles in one of four directions (**left, right, up, or down**) to merge identical values. Each move increases the player’s score based on the sum of merged tiles.  

### **Understanding the Minimax Algorithm**  

The **Minimax algorithm** is a fundamental decision-making approach in **game theory and AI**, commonly used in two-player games like **Chess** and **Tic-Tac-Toe**. The algorithm constructs a **game tree**, where:  

- Each **node** represents a possible game state.  
- Each **edge** represents a possible move (in 2048: left, right, up, down).  
- The AI **maximizes** its advantage while assuming the opponent will **minimize** it.  

Minimax recursively evaluates possible moves until reaching a **terminal state** (end of the game or a predefined depth). The algorithm then selects the **optimal move** based on the highest heuristic value.  

---  

## **Methodology**  

### **Constructing the Board**  

The first step was implementing a **Board class** to handle 2048’s game logic. Key features include:  

- **Move Functions** – Implementing movement logic efficiently using **transpose/reversal** techniques.  
- **Tile Placement** – Adding tiles by checking for **available empty spaces**.  
- **Move Availability Checks** – Essential for determining **child nodes** in the game tree.  

### **Implementing Minimax in 2048**  

2048 is **traditionally a single-player game**, so I had to define **what to maximize and minimize**. Many research papers treat the **random tile placements** as the minimizing factor, requiring an **expectimax variant** of Minimax to handle uncertainty. However, I opted for a **deterministic two-player adaptation**, where:  

- **The AI player maximizes optimal moves**.  
- **An adversarial player (Minimizer) selects the least optimal move**.  

This **simplified implementation**, making the search space **fully deterministic** by:  

- Removing **random tile placements**.  
- Making the **addTile()** function always place a **4 tile** in the first available space.  

This approach eliminated the need for **alpha-beta pruning**, which would have been necessary in an **expectimax model**.  

### **Implementing Minimax**  

The Minimax algorithm was implemented following this **pseudo-code logic**:  

```python
# Minimax Function
function minimax(state, depth, isMaximizingPlayer):
    if depth == 0 or game_over(state):
        return heuristic(state)
    
    if isMaximizingPlayer:
        bestValue = -inf
        for child in get_children(state):
            val = minimax(child, depth - 1, False)
            bestValue = max(bestValue, val)
        return bestValue
    else:
        bestValue = +inf
        for child in get_children(state):
            val = minimax(child, depth - 1, True)
            bestValue = min(bestValue, val)
        return bestValue
```  

---  

## **Heuristic Function Design**  

One of the most challenging aspects was **designing an effective heuristic function**. Research showed that there is no universal "meta" heuristic for 2048. However, the most common approaches include:  

1. **Weighted Grid Heuristic**  
   - Assigns **higher weights to corners**, encouraging **large tiles** to be positioned optimally.  
   - Uses a **dot product** between the board state and a weight matrix.  

2. **Empty Space Heuristic**  
   - Rewards game states with **more empty tiles**, allowing **greater move flexibility**.  

3. **Unique Tile Penalty**  
   - Penalizes game states with **too many distinct tile values**, encouraging **fewer unique tiles** for easier merging.  

My final heuristic function combined these principles:  

```
H = A * E - B * D - C * P
```

Where:  

- **E** = Number of **empty spaces** (encourages move flexibility).  
- **D** = Number of **unique tiles** (penalizes disorganized boards).  
- **P** = Indicator if the **largest tile is in the corner** (rewards structured play).  
- **A, B, C** = Tunable constants.  

This function effectively balances **empty space priority, tile organization, and corner placement**, optimizing AI decision-making.  

---  

## **Results & Analysis**  

I conducted **six trials**, adjusting parameters to analyze their impact on **node expansion, generation, and tile progression**.  

<img width="635" alt="Screenshot 2023-05-02 at 2 41 34 PM" src="https://user-images.githubusercontent.com/120329214/235757295-0a42897c-cbc8-47c3-8089-649d8a81edf7.png">

Key insights:  

- **Greater search depth increases node generation**, improving decision-making.  
- **Nodes expanded remained stable despite depth increases**, indicating efficient move pruning.  
- **Unique tile penalty (high B value) drastically reduced game longevity**, leading to only **43 node expansions** before failure.  

---  

## **Conclusion**  

This project successfully **deepened my understanding of Minimax** and its application to **game AI**. Key takeaways include:  

- **Search depth significantly impacts decision quality** but does not always increase node expansion.  
- **Heuristic function tuning is critical**, with different weight distributions leading to varied AI behaviors.  
- **An adversarial opponent severely limits tile progression**, often capping at **512 tiles**.  

### **Future Improvements**  

Given more time, I would:  

- **Enhance the UI with graphics** for better visualization.  
- **Allow parameter tuning** for **real-time heuristic adjustments**.  
- **Implement the Expectimax model** to account for randomness and evaluate AI performance based on **highest score** instead of tile progression.  

---

