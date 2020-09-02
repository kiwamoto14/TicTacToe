
board = {
    '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'
}

chosenSpace = []

def printBoard():
    print(board['1'], "|", board['2'], "|", board['3'])
    print("----------")
    print(board['4'], "|", board['5'], "|", board['6'])
    print("----------")
    print(board['7'], "|", board['8'], "|", board['9'])

def checkEmpty(selection, turn):
    if (board[selection] == 'X' or board[selection] == 'O'):
        return False
    else:
        return True

def checkWin():
    if board['1'] == board['2'] == board['3']:
        win = True
    elif board['4'] == board['5'] == board['6']:
        win = True
    elif board['7'] == board['8'] == board['9']:
        win = True
    elif board['1'] == board['4'] == board['7']:
        win = True
    elif board['2'] == board['5'] == board['8']:
        win = True
    elif board['3'] == board['6'] == board['9']:
        win = True
    elif board['1'] == board['5'] == board['9']:
        win = True
    elif board['3'] == board['5'] == board['7']:
        win = True
    else:
        win = False

    return win

if __name__ == "__main__":
    win = False
    count = 0
    turn = 'O'
    empty = True
    while count < 9 and win == False:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        printBoard()
        print("\nIt is " + turn + "'s turn")
        userinput = input("Please make your selection: ")

        while userinput != '1' and userinput != '2' and userinput != '3' and userinput != '4' and userinput != '5' and userinput != '6' and userinput != '7' and userinput != '8' and userinput != '9' :
            userinput = input("That is not a valid selection. Please choose again: ")

        empty = checkEmpty(str(userinput), turn)

        while empty == False:
            userinput = input("That space has already been chosen. Please choose again: ")
            empty = checkEmpty(userinput, turn)

        board[str(userinput)] = turn
        win = checkWin()
        count += 1

    printBoard()
    if win == True:
        print("Congratulations! " + turn + " has won the game!")
    else:
        print("This game has ended in a tie")
