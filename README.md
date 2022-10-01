# TIC-TAC-TOE
## Problem Statement
An AI algorithm based Tic-Tac-Toe.

## Description
In order to build this game, we have made use of the *Minimax* algorithm. This is a recursive algorithm that enables the AI agent to choose the most optimum move based on all the subsequent moves that could take place in the further turns of the game. 

We used pygame library to develop this game

## Features of the Application

1. **3X3 tic-tac-toe:** <br/>
The 3x3 tic-tac-toe is built with incremental levels of difficulty. A different algorithmic approach is used to attribute smartness to the agent at each level. The ultimate level is unbeatable and will always result in either a WIN of the agent or a TIE.

2. **Comfortable gameplay**<br/>
The application also consists of an indicator on the top bar of the board denoting who's turn it is.

## 3x3 TicTacToe

Our idea revolves around directing the AI agent (in this case the computer) to choose a move based on the utilities of the immediate next moves available to it. The agent must pick the maximum of these utilities for the next move.

## Rules for 3x3

There are 9 cells in 3*3 tic-tac-toe board, which are numbered sequentially from 0 to 8.

* Start by selecting a player who shall begin the game
* The robot and the human play in alternation
* First person to get their symbol across an entire row, column or diagonal wins

For instance, suppose the agent is about to place its move in the cell [0], if permitted, it can win in three ways 
* Horizontally : by placing in cells 1 and 2 
* Vertically       : by placing in cells 3 and 6 
* Diagonally    : by placing in cells 4 and 8 
