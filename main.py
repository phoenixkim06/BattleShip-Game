import numpy as np
import sys
import math
import random
from random import randint

row_count = 10
col_count = 10

# Board where code happens
board = []
for x in range(10):
    board.append(["0"] * 10)


def print_board(board):
    for row in board:
        print(" ".join(row))


# Board for visuals
visualBoard = []
for x in range(10):
    visualBoard.append(["0"] * 10)


def print_visualBoard(visualBoard):
    for row in visualBoard:
        print(" ".join(row))


shipCoordinates = None


def createRandomShips(board, ship, ship2, ship3):
    # getting random point and direction
    rand_row = randint(1, row_count - 2)
    rand_col = randint(1, col_count - 2)
    board[rand_row][rand_col] = ship
    if rand_row == 1:
        direction = 2
    elif rand_row == 8:
        direction = 1
    elif rand_col == 1:
        direction = 4
    elif rand_col == 8:
        direction = 3
    else:
        direction = random.randrange(1, 4)

    # for at the ends of rows w/ directions
    if rand_row >= 8 and direction == 2:
        extensionNumber = 2
    elif rand_row == 7 and direction == 2:
        extensionNumber = 3
    elif rand_row == 6 and direction == 2:
        extensionNumber = random.randrange(3, 4)
    elif rand_row == 3 and direction == 1:
        extensionNumber = random.randrange(2, 4)
    elif rand_row == 2 and direction == 1:
        extensionNumber = random.randrange(2, 3)
    elif rand_row == 1 and direction == 1:
        extensionNumber = 2
    # for at the ends of columns w/ directions
    elif rand_col >= 8 and direction == 4:
        extensionNumber = 2
    elif rand_col == 7 and direction == 4:
        extensionNumber = 3
    elif rand_col == 6 and direction == 4:
        extensionNumber = random.randrange(3, 4)
    elif rand_col == 3 and direction == 3:
        extensionNumber = random.randrange(2, 4)
    elif rand_col == 2 and direction == 3:
        extensionNumber = random.randrange(2, 3)
    elif rand_col == 1 and direction == 3:
        extensionNumber = 2
    else:
        extensionNumber = random.randrange(3, 5)

    # extending randomly
    if direction == 1:  # up
        for i in range(1, extensionNumber):
            board[rand_row - i][rand_col] = ship

    elif direction == 2:  # down
        for i in range(1, extensionNumber):
            board[rand_row + i][rand_col] = ship

    elif direction == 3:  # left
        for i in range(1, extensionNumber):
            board[rand_row][rand_col - i] = ship

    else:  # right
        for i in range(1, extensionNumber):
            board[rand_row][rand_col + i] = ship

    # ship #2
    # All variables changed to 2
    rand_row2 = randint(1, row_count - 2)
    rand_col2 = randint(1, col_count - 2)
    # as long as the new ship's starting point doesnt fall on a previous ship, continue. Otherwise assign new value(s) until it doesnt.
    while board[rand_row2][rand_col2] != "0":
        # rand_row2 == rand_row and rand_col2 == rand_col:
        rand_row2 = randint(1, row_count - 2)
        rand_col2 = randint(1, col_count - 2)

    board[rand_row2][rand_col2] = ship2

    if rand_row2 == 1:
        direction2 = 2
    elif rand_row2 == 8:
        direction2 = 1
    elif rand_col2 == 1:
        direction2 = 4
    elif rand_col2 == 8:
        direction2 = 3
    else:
        direction2 = random.randrange(1, 4)

        # for at the ends of rows w/ directions
    if rand_row2 >= 8 and direction2 == 2:
        extensionNumber2 = 2
    elif rand_row2 == 7 and direction2 == 2:
        extensionNumber2 = 3
    elif rand_row2 == 6 and direction2 == 2:
        extensionNumber2 = random.randrange(3, 4)
    elif rand_row2 == 3 and direction2 == 1:
        extensionNumber2 = random.randrange(2, 4)
    elif rand_row2 == 2 and direction2 == 1:
        extensionNumber2 = random.randrange(2, 3)
    elif rand_row2 == 1 and direction2 == 1:
        extensionNumber2 = 2
        # for at the ends of columns w/ directions
    elif rand_col2 >= 8 and direction2 == 4:
        extensionNumber2 = 2
    elif rand_col2 == 7 and direction2 == 4:
        extensionNumber2 = 3
    elif rand_col2 == 6 and direction2 == 4:
        extensionNumber2 = random.randrange(3, 4)
    elif rand_col2 == 3 and direction2 == 3:
        extensionNumber2 = random.randrange(2, 4)
    elif rand_col2 == 2 and direction2 == 3:
        extensionNumber2 = random.randrange(2, 3)
    elif rand_col2 == 1 and direction2 == 3:
        extensionNumber2 = 2
    else:
        extensionNumber2 = random.randrange(3, 5)

    # check if the spot already is assigned to a value (break) or if not assign new value

    # check if the spot already is assigned to a value (break) or if not assign new value
    # truncate ship sizes if needed
    if direction2 == 1:  # up
        for i in range(1, extensionNumber2):
            if board[rand_row2 - i][rand_col2] == ship:
                break
            else:
                board[rand_row2 - i][rand_col2] = ship2

    elif direction2 == 2:  # down
        for i in range(1, extensionNumber2):
            if board[rand_row2 + i][rand_col2] == ship:
                break
            else:
                board[rand_row2 + i][rand_col2] = ship2

    elif direction2 == 3:  # left
        for i in range(1, extensionNumber2):
            if board[rand_row2][rand_col2 - i] == ship:
                break
            else:
                board[rand_row2][rand_col2 - i] = ship2

    else:  # right
        for i in range(1, extensionNumber2):
            if board[rand_row2][rand_col2 + i] == ship:
                break
            else:
                board[rand_row2][rand_col2 + i] = ship2

    # 3rd ship
    rand_row3 = randint(1, row_count - 2)
    rand_col3 = randint(1, col_count - 2)
    # as long as the new ship's starting point doesnt fall on a previous ship, continue. Otherwise assign new value(s) until it doesnt.
    while board[rand_row3][rand_col3] != "0":
        rand_row3 = randint(1, row_count - 2)
        rand_col3 = randint(1, col_count - 2)
    board[rand_row3][rand_col3] = ship3
    if rand_row3 == 1:
        direction3 = 2
    elif rand_row3 == 8:
        direction3 = 1
    elif rand_col3 == 1:
        direction3 = 4
    elif rand_col3 == 8:
        direction3 = 3
    else:
        direction3 = random.randrange(1, 4)
    # print("checkpoint")
    if rand_row3 >= 8 and direction3 == 2:
        extensionNumber3 = 2
    elif rand_row3 == 7 and direction3 == 2:
        extensionNumber3 = 3
    elif rand_row3 == 6 and direction3 == 2:
        extensionNumber3 = random.randrange(3, 4)
    elif rand_row3 == 3 and direction3 == 1:
        extensionNumber3 = random.randrange(2, 4)
    elif rand_row3 == 2 and direction3 == 1:
        extensionNumber3 = random.randrange(2, 3)
    elif rand_row3 == 1 and direction3 == 1:
        extensionNumber3 = 2
        # for at the ends of columns w/ directions
    elif rand_col3 >= 8 and direction3 == 4:
        extensionNumber3 = 2
    elif rand_col3 == 7 and direction3 == 4:
        extensionNumber3 = 3
    elif rand_col3 == 6 and direction3 == 4:
        extensionNumber3 = random.randrange(3, 4)
    elif rand_col3 == 3 and direction3 == 3:
        extensionNumber3 = random.randrange(2, 4)
    elif rand_col3 == 2 and direction3 == 3:
        extensionNumber3 = random.randrange(2, 3)
    elif rand_col3 == 1 and direction3 == 3:
        extensionNumber3 = 2
    else:
        extensionNumber3 = random.randrange(3, 5)

    # check if the spot already is assigned to a value (break) or if not assign new value
    # truncate ship sizes if needed

    if direction3 == 1:  # up
        for i in range(1, extensionNumber3):
            if board[rand_row3 - i][rand_col3] == ship or board[rand_row3 - i][rand_col3] == ship2:
                break
            else:
                board[rand_row3 - i][rand_col3] = ship3

    elif direction3 == 2:  # down
        for i in range(1, extensionNumber3):
            if board[rand_row3 + i][rand_col3] == ship or board[rand_row3 + i][rand_col3] == ship2:
                break
            else:
                board[rand_row3 + i][rand_col3] = ship3

    elif direction3 == 3:  # left
        for i in range(1, extensionNumber3):
            if board[rand_row3][rand_col3 - i] == ship or board[rand_row3][rand_col3 - i] == ship2:
                break
            else:
                board[rand_row3][rand_col3 - i] = ship3

    else:  # right
        for i in range(1, extensionNumber3):
            if board[rand_row3][rand_col3 + i] == ship or board[rand_row3][rand_col3 + i] == ship2:
                break
            else:
                board[rand_row3][rand_col3 + i] = ship3


createRandomShips(board, "1", "2", "3")
winner = False
# function for guessing row & col values.
shipsSunk = []


def guessShips(guessRow, guessCol):
    # if guessed before, try again
    global guessCount
    global winner

    if board[int(guessRow)][int(guessCol)] == "A" or board[int(guessRow)][int(guessCol)] == "X":
        print_visualBoard(visualBoard)
        print("Already guessed, try again.")
    # if new guess and miss, count as miss and change the value on the board to an A
    elif board[int(guessRow)][int(guessCol)] == "0":
        board[int(guessRow)][int(guessCol)] = "A"
        # print out visual board with A
        visualBoard[int(guessRow)][int(guessCol)] = "A"
        print_visualBoard(visualBoard)
        guessCount -= 1
        print("Row:", guessRow, "Col:", guessCol, "-", "Missed, try again.")
    # if new guess and hit, count as hit and change the value on the board to an X
    # check the values for each piece and if all the ships have been guessed, then the player wins.

    elif board[int(guessRow)][int(guessCol)] == "1" or board[int(guessRow)][int(guessCol)] == "2" or \
            board[int(guessRow)][int(guessCol)] == "3":
        board[int(guessRow)][int(guessCol)] = "X"
        # print out visual board with X
        visualBoard[int(guessRow)][int(guessCol)] = "X"
        print_visualBoard(visualBoard)
        guessCount -= 1
        print("Row:", guessRow, "Col:", guessCol, "-", "Hit")
        # list with all pieces on the board
        allpieces = []
        for i in range(0, row_count):
            for j in range(0, col_count):
                allpieces.append(board[i][j])
        # if 1s or 2s or 3s not on board then sunk ships
        if "1" not in allpieces:
            shipsSunk.append("Ship 1")
            winner = False
        if "2" not in allpieces:
            shipsSunk.append("Ship 2")
            winner = False
        if "3" not in allpieces:
            shipsSunk.append("Ship 3")
            winner = False
        # if the board has 1 2 3 (ships) then no winner. otherwise winner = true
        if "1" in allpieces or "2" in allpieces or "3" in allpieces:
            winner = False
        else:
            winner = True
            print("You Win!")

    print("Ships sunk:")
    if shipsSunk:
        print(", ".join(set(shipsSunk)))
    else:
        print("None")


print("Welcome to Battleship. The goal of the game is to sink all the ships before your guesses run out.")
print("Difficulties: \n 1: Easy \n 2: Medium \n 3: Hard")
# print("1: Easy")
# print("2: Medium")
# print("3: Hard")
difficulty = input("Choose from the difficulties listed above by entering in 1, 2, or 3: ")
difficultyRange = range(1, 4)
if difficulty.isdigit():
    if int(difficulty) in difficultyRange:
        difficulty = int(difficulty)
    else:
        while int(difficulty) not in difficultyRange:
            difficulty = int(input("Invalid difficulty. Choose a difficulty 1, 2, or 3: "))
else:
    while not difficulty.isdigit():
        difficulty = input("Invalid difficulty. Choose a difficulty 1, 2, or 3: ")

if int(difficulty) == 1:
    guessCount = 40
elif int(difficulty) == 2:
    guessCount = 35
elif int(difficulty) == 3:
    guessCount = 30
print_visualBoard(visualBoard)
# while there are still guesses left and there is no winner, continue playing the game
while winner == False:
    # ask for input from the user for a row and col value
    # print the board
    if guessCount > 0:
        guessRow = input("Enter in a row value: ")
        guessCol = input("Enter in a column value: ")
        guessRange = range(0, 10)
        if guessRow.isdigit():
            while int(guessRow) not in guessRange:
                guessRow = int(input("Invalid row value. Enter in a row value between 0-9: "))
        else:
            while not guessRow.isdigit():
                guessRow = input("Invalid row value. Enter in a row value between 0-9: ")

        if guessCol.isdigit():
            while int(guessCol) not in guessRange:
                guessCol = int(input("Invalid column value. Enter in a column value between 0-9: "))

        else:
            while not guessCol.isdigit():
                guessCol = input("Invalid column value. Enter in a column value between 0-9: ")

        guessShips(guessRow, guessCol)
    else:
        print("You Lose - Ran Out of Tries")
        print("Correct board:")
        print_board(board)
        break
    print("Guesses remaining:", guessCount)
