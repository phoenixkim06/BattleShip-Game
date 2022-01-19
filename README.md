#Battleship Game
Battleship is a single-player console-based game where the user tries to sink all 3 battleships before they run out of tries.
###The Board:

The playing board is a 10x10 grid with 3 ships of random sizes (1, 2, 3, or 4 pieces) all spaced out randomly. Each ship will be hidden but will either be indicated with a 1, 2, or 3 value.

When the user hits a ship, the corresponding piece on the board will update with an X. If it is a miss, the piece will update to an A.

##To play:

1. The user begins by inputting either a difficulty
    - 1 = Easy (40 guesses)
    - 2 = Medium (35 guesses)
    - 3 = Hard (30 guesses)

2. Then the user is asked to input in a row and column value. If either are invalid, the console will prompt the user to input in a new value.

3. At the end of each turn, the console will display: 
    - the board with visuals
    - a message on whether they:
        - hit/missed a ship
        - repeated a guess and need to retry
    - the total ships sunk
    - guesses remaining

***These steps will repeat until the user either sinks all ships (win) or runs out of guesses (lose)***
###Sample Turns:
```sh
Welcome to Battleship. The goal of the game is to sink all the ships before your guesses run out.
Difficulties: 
 1: Easy 
 2: Medium 
 3: Hard
Choose from the difficulties listed above by entering in 1, 2, or 3: 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
Enter in a row value: 3
Enter in a column value: 13
Invalid column value. Enter in a column value between 0-9: 3
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 A 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
Row: 3 Col: 3 - Missed, try again.
Ships sunk:
None
Guesses remaining: 39
Enter in a row value: 5
Enter in a column value: 7
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 A 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 X 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
Row: 5 Col: 7 - Hit
Ships sunk:
None
Guesses remaining: 38
Enter in a row value: 
```

###Todos:
- [ ] Add a feature to create a consistent balance of ship sizes
- [ ] Prevent the Ships sunk status message and guesses remaining message from appearing after a win
