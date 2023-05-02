# 2048classicalAI

Introduction

I have always found the topic of Artificial Intelligence interesting, especially when it came to games. I would spend a lot of time during my undergrad watching videos of an AI being trained to play games like Mortal Kombat or Streetfighter. My senior year, I took my first course on AI which was where I was introduced to the minimax algorithm. I learned how it utilized recursion and backtracking to make decisions in problems relating to game theory. Although I understood what the algorithm was used for, I had little knowledge about how to implement it, or how it worked at a high level. I knew enough to fill out a minimax graph, but that was about it.

This project was an opportunity for me to further my understanding of the minimax algorithm which I had covered in college. The best way to do that is to practice implementing it on a game with a reasonably sized search space. For this project, I decided to go with the game 2048.

Background

Understanding 2048
In the game 2048, the objective is to slide numbered tiles across a board to combine them. We repeat this process of merging tiles until we have a 2048 tile on the board. To start, the game initially has two tiles on the board with values of 2 or 4. When moving the tiles in a particular direction, all the tiles on the grid that share the same value will merge into one tile equal to the sum of their respective values. Typically, the game also keeps track of the players score, which grows as the player combines tiles. The points are the value of the resulting merged tiles that get added to the total score.

Understanding the Minimax Algorithm
The minimax algorithm is a decision-based algorithm typically used in game theory and artificial intelligence. The idea is that the algorithm can find the most optimal move for a player in a two-player game such as chess, or tic-tac-toe. In finding the optimal move for one player, the algorithm is also finding the least optimal path for the other player.

The algorithm works by creating a game tree graph, where each node represents a game state, and each edge represents a potential move which in this case would be a slide direction (left, right, up, down). At each node in the game tree, the algorithm determines the heuristic value of each potential move, by assuming the opponent will pick the most disadvantageous moves for the current player. The algorithm continues to search the game tree, switching between maximizing and minimizing steps until it reaches the end of the game tree or a predetermined depth (which we call the terminal states). After calculating the heuristic of these terminal states, minimax will then try and choose the move that results in the highest heuristic value for the current player. 

Methodology

Constructing the Board
The first step in this project was constructing the board class to implement the game 2048. The first few functions in the class allow the board to be moved in each direction. There was only a need to make a function that moved the board left since the up, down, and right moves could be done by transposing/reversing the board. There were also a few functions that added a tile to the board by checking the available empty spaces. Most functions in the class are there to check the availability of moves in each direction on the board. This was necessary to determine the child nodes.

Implementing 2048
Since 2048 is typically a one player game, I had to figure out what was going to be maximized and minimized. In some of the research papers I read about implementing minimax into 2048, many people would treat the randomness of the tiles being placed as the thing being minimized. They would then maximize the potential directions the board can move. I didn’t want to follow this way of thinking because it would require the use of the expected minimax algorithm to deal with the uncertainty of the tiles. Instead, I thought it would be more beneficial to make the game a typical two player game where one player is consistently trying to choose the least optimal move. This methodology would keep the implementation of the algorithm straight forward and it would reduce our search space significantly. If I had taken the expected minimax route, I would probably also implement alpha-beta pruning to reduce the size of the search tree. The benefit of going that route would be the fact that we could have different results each time we played the game due to the randomness of how the tiles get added.

Since I decided to stick with the two-player implementation of the algorithm, I had to remove the randomness of the tiles to make the search space deterministic. I simply made the “addTile” function iterate through each row and column of the board and append the empty spaces to a list. The function would always select the first element in the list to add a tile. I also made the function always add a 4 tile to the board to keep everything consistent.

When it came to coding the minimax algorithm, I pretty much just followed the logic of this pseudocode:

 

Heuristic
The portion of this project that I spent the most amount of time on, was figuring out what heuristic function I wanted to use. After doing numerous amounts of research, I reached the conclusion that there wasn’t a “meta” heuristic that was used for the game 2048. Most people used a matrix that had higher weights in the corners. They would get the sum product of the matrix and the game board and use that as the heuristic value. The matrix is supposed to reward moves that result with larger valued tiles in the corner. These particular game-states provide the best opportunity of winning since the max tiles can remain in one specific location the duration of the game. 
 

The other heuristic function I found rewards moves that result in more empty spaces on the board. The logic here is that when there is more space available, there are more potential moves that can be made. More space on the board also means that we are rewarding moves that merge multiple tiles.

 
I wanted to use a heuristic function that encompassed all the traits that were listed above.  I slightly altered the heuristic function used in one research paper which left me with the following equation:

H = A*E – B*D – C*P

A, B, and C are all constants. E is the number of empty weights on the board, D is the number of unique tiles, and P is an indicator of whether the maximum tile on the board is in the corner. With this function, there is also a component which rewards moves that result in fewer unique tiles. The logic behind this was to put a larger emphasis on game states that had a higher potential to merge tiles.

Results and Analysis

For my project, I ran six trials. Each trial I changed one parameter to see how it affected the results. The way I evaluated each trial was by looking at the number of nodes expanded, the number of nodes generated, and the largest tile. 

Based on the data, I think that the results are what I’d expect. The greater the depth size, the greater the number of nodes generated. I was surprised to see that the number of nodes expanded did not increase with depth size. I think that this makes sense due to the game being able to make better decisions by looking further ahead into the future.

I was also surprised to see that only 43 nodes were expanded when the highest weight was put on constant B. This tells me that the aspect of the heuristic function which focuses on the number of unique tiles isn’t too important. The nodes only get expanded 43 times because the game ends so quickly.

Conclusion

I think the project was successful. Given that I was evaluating the performance of the algorithm on the number of nodes expanded and generated, the results were within my expectations. I was surprised to see that through five of the six trials, the highest tile was only 512. This is more than likely due to the minimizing player who chooses the least optimal move on their turn. Given additional time, I would have added graphics to make the presentation more visually appealing. I also would have given the user the ability to adjust the parameters of the heuristic function or alter characteristics of the board. It would have been cool to also implement the expected minimax version of 2048 so that I could evaluate the model based on the highest score. 
