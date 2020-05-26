list1 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
def printer(a,sym =" "):
    list2 = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    if list1[a-1] == " ":
        list1[a-1]=sym
    b=0
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            list2[i][j] = list1[b]
            b += 1
            if j < 2:
                print(" ", list2[i][j], " ", end="|")
            else:
                print(" ", list2[i][j], " ", end=" ")
        print()
        if i < 2:
            print("-----|-----|-----")
        else:
            print(" ")
    return list1
def check(list3,symbol):
        if list3[0] == list3[3] == list3[6] == symbol or list3[1] == list3[4] == list3[7] == symbol or list3[2] == list3[5] == list3[8] == symbol:
            return 'you win'
        elif list3[0] == list3[1] == list3[2] == symbol or list3[3] == list3[4] == list3[5] == symbol or list3[6] == list3[7] == list3[8] == symbol:
            return 'you win'
        elif list3[0] == list3[4] == list3[8] == symbol or list3[2] == list3[4] == list3[6] == symbol:
            return 'you win'
        elif check_full_board(list1) == ' board is full ':
            return " it's a draw "
        else:
            return 'next turn'

def check_full_board(board):
    flag=0
    for i in range(0,9,1):
        if board[i] != " ":
            flag = 1
    if flag == 1:
        return board
    else:
        return ' board is full '

def player_input():
    marker = ' '
    while marker != 'X' and marker != 'O':
        marker = input("player one choose 'X' or 'O'").upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

import random
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'player 1'
    else:
        return 'player 2'

ans = 'y'
while ans == 'y' or ans == 'Y':
    Player = input(" press any key to start ----->")
    printer(0)
    player1_marker, player2_marker = player_input()
    turn=choose_first()
    print(turn+' plays first')
    count = 0
    while count <= 9:
        if turn == 'player 1':
            Player1=int(input("Player 1 enter the position --->"))
            printer(Player1, player1_marker)
            if check(list1,player1_marker) == 'you win':
                print(check(list1, player1_marker))
                break
            turn = 'player 2'
        else:
            Player2=int(input("PLayer 2 enter the position --->"))
            printer(Player2, player2_marker)
            if check(list1,player2_marker) == 'you win':
                print(check(list1, player2_marker))
                break
            turn = 'player 1'
        count += 1
    ans = input("do you want to play again press y/n---->")