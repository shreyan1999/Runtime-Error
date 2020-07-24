# Tic Tac Toe using Minimax Algorithm.

## **_Algorithm Basics_**

   Minimax Algorithm is a backtracking algorithm that is used in game theory to find the optimal move for a player assuming that your opponent also plays optimally.Its basically a computer playing against a computer.To solve the problem of optimization a heuristic function is involved.The heuristic function is basically a way to inform the search about the direction to a goal.<br />
   Alpha-Beta Pruning is also used which is not actually an algorithm rather an optimization technique.It reduces the computation time of the tree by a huge factor.This also allows us to search faster and even go into deeper levels in the game tree by cutting off few branches.<br />
      
    
*The pseudocode is as follows:*

```
function minimaxDecision (game)
	for each possible move in game
		moveValue = minimaxValue(state, game)

	return move with highest value

function minimaxValue (state, game)
	if terminal node
		return utility

	if player 1's turn
		return highest value of children

	if player 2's turn
		return lowest value of children
  ```
 

*The minimax tree is as follows:*

![Image of Minimax Tree](https://www.researchgate.net/publication/262672371/figure/fig1/AS:393455625883662@1470818539933/Game-tree-for-Tic-Tac-Toe-game-using-MiniMax-algorithm.png)

## **_About the Website_**

   We have used simple HTML,CSS and JavaScript for the basic website rendering.We have chosen Client side rendering for the basic website to reduce the latency and improve the gaming experience.There are also a few elements of bootstrap included.<br />

For multiplayer mode and Chatapp Socket.IO , Node.js, jQuery, Express.js are used.
<br />
 
 Team Name: **RUNTIME ERROR**
 -  Team from Manipal Institute of Technology,Manipal.
 -  Team Members:
    * Shreyan J D Fernandes 
    * Pranathi Kanamarlapudi
