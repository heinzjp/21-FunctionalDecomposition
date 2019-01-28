"""
Hangman.

Authors: Justin Heinz and Rishav R Khosla.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.

import random


def check_game(board):
    for k in range(len(board)):
        if board[k] == '_':
            return False
    return True


def quit_game(word, board):
    if check_game(board):
        print('You win!')
    else:
        print('You lose! The secret word was ', word)
    ans = input('Play another game? (y/n) ')
    if ans is 'y':
        main()
    else:
        print('Thanks for playing hangman!')


def print_board(list_board):
    for j in range(len(list_board)):
        print(list_board[j] + ' ', end='')
    print()


def change_board(word, guess, board):
    for k in range(len(word)):
        if guess == word[k]:
            board[k] = guess
    return board


def check_guess(word, guess, n, board):
    for k in range(len(word)):
        if guess == word[k]:
            print('Good Guess!')
            print()
            return True
    print()
    print('Sorry there is no letter', guess, 'in the secret word.')
    print_board(board)
    if n > 1:
        print('You still have ', n - 1, ' unsuccessful guesses left before you LOSE the game!')
    print()
    return False


def create_board(word):
    board = '_ ' * len(word)
    print(board)
    return board


def get_word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
        r = random.randrange(0, len(words))
        word = words[r]
        return word


def main():
    print()
    word = get_word()
    board = create_board(word)
    board = board.split()
    n = int(input('How many unsuccessful choices do you want to allow yourself? '))
    while True:
        guess = str(input('What letter do you want to try? '))
        answer = check_guess(word, guess, n, board)
        if answer:
            board = change_board(word, guess, board)
            print_board(board)
        elif answer is False:
            n = n - 1
        if n == 0 or check_game(board):
            quit_game(word, board)
            break


def introduction():
    print('I will choose ea random secret word form a dictionary.')
    print('You will set the MINIMUM length of the word.')
    print()
    print('You will set the difficulty of the game.')
    print('---------------------------------------------------------')


introduction()
main()

####### Do NOT attempt this assignment before class! #######