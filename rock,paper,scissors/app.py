from random import randint

choices = ['rock', 'paper', 'scissors']
computer = choices[randint(0, 2)]
player = False
while not player:
    player = input('make a move.rock, paper, scissors: ')
    if player == computer:
        print('tie')
    elif player == 'rock':
        if computer == 'paper':
            print('computer wins')
        else:
            print('you won')
    elif player == 'scissors':
        if computer == 'paper':
            print('you won')
        else:
            print('computer wins')
    elif player == 'paper':
        if computer == 'rock':
            print('you won')
        else:
            print('computer wins')
    else:
        print('invalid input')
    player=False
    computer=choices[randint(0,2)]
