import numpy as np
from connect4_ai import *

ROW_SIZE = 6
COLUMN_SIZE = 7

board = np.full((ROW_SIZE, COLUMN_SIZE), -1)
column_index = [0 for num in range(COLUMN_SIZE)]

menu_str = "1 ~ 7번 중 컬럼 선택하세요."

"""AI는 0번, 사용자는 1번입니다."""
"""-1은 빈칸, 0은 AI, 1은 사용자입니다."""


def print_board():
    for row in range(len(board)):
        for column in range(len(board[ROW_SIZE - 1 - row])):
            if board[ROW_SIZE - 1 - row][column] == 0:
                print('|0', end='')
            elif board[ROW_SIZE - 1 - row][column] == 1:
                print('|X', end='')
            else:
                print('| ', end='')
        print("|")


def choose(column, user=0):
    column -= 1
    if column_index[column] >= ROW_SIZE or column < 0 or column >= COLUMN_SIZE:
        return False

    board[column_index[column]][column] = user
    column_index[column] += 1
    print_board()
    return True


def is_game_over(user):
    for column in range(COLUMN_SIZE - 3):
        for row in range(ROW_SIZE):
            if board[row][column] == user and board[row][column + 1] == user and board[row][column + 2] == user and \
                    board[row][column + 3] == user:
                return True

    for column in range(COLUMN_SIZE):
        for row in range(ROW_SIZE - 3):
            if board[row][column] == user and board[row + 1][column] == user and board[row + 2][column] == user and \
                    board[row + 3][column] == user:
                return True

    for column in range(COLUMN_SIZE - 3):
        for row in range(ROW_SIZE - 3):
            if board[row][column] == user and board[row + 1][column + 1] == user and board[row + 2][
                column + 2] == user and board[row + 3][column + 3] == user:
                return True

    for column in range(COLUMN_SIZE - 3):
        for row in range(3, ROW_SIZE):
            if board[row][column] == user and board[row - 1][column + 1] == user and board[row - 2][
                column + 2] == user and board[row - 3][column + 3] == user:
                return True


first_person = int(input("선공:1, 후공:2  선택하세요. :"))
if first_person == 1:
    while True:
        i = int(input(menu_str))
        while True:
            if(i!=4):
                break
            print("선공은 4번 컬럼에 놓을수 없습니다")
            i = int(input(menu_str))4
        if choose(i, 1):
            break

while True:
    print("AI가 밑에 처럼 놓았습니다.")
    while True:
        choice_ai = ai(board)
        if choose(choice_ai):
            break

    if is_game_over(0):
        print("AI가 승리하였습니다.")
        break

    while True:
        i = int(input(menu_str))
        if choose(i, 1):
            break

    if is_game_over(1):
        print("당신이 승리하였습니다.")
        break
