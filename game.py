import random

try:
    file = open('rating.txt', 'x')
except FileExistsError:
    file = open('rating.txt', 'r')

list_lines = file.read().split('\n')
list_scores = [int(i.split(' ')[1]) for i in list_lines]
list_names = [i.split(' ')[0] for i in list_lines]
file.close()

name = input('Enter your name: ')
print(f'Hello, {name}')

if name in list_names:
    score = [int(i.split(' ')[1]) for i in list_lines]
else:
    score = 0

options = input()
print("Okay, let's start")
default_options = ['paper', 'scissors', 'rock', '!exit', '!rating']
computer_options = ['paper', 'scissors', 'rock']
if options == '':
    computer_options = ['paper', 'scissors', 'rock']
else:
    computer_options = options.split(',')

scores = dict(zip(list_names, list_scores))
someones_score = 0


def turn(user_input, computer_input):
    if user_input == computer_input:
        print(f'There is a draw ({user_input})')
        return 50
    elif computer_input in win_list:
        print(f'Sorry, but the computer chose {computer_input}')
        return 0
    elif computer_input in loose_list:
        print(f'Well done. The computer chose {computer_input} and failed')
        return 100
    return 0


def print_score():
    if name in scores:
        print(f'Your rating: {scores[name]}')
    else:
        print(f'Your rating: {someones_score}')


while True:
    user_input = input()
    computer_input = random.choice(computer_options)
    if user_input == '!exit':
        print('Bye!')
        break
    elif user_input == '!rating':
        print_score()
    elif user_input in computer_options:
        index_user_choice = computer_options.index(user_input)
        new_list = computer_options[index_user_choice + 1:] + computer_options[: index_user_choice]
        index_slice = int(len(new_list) / 2)
        win_list = new_list[:index_slice]
        loose_list = new_list[index_slice:]
        score = turn(user_input, computer_input)
        if name in scores:
            scores[name] += score
        else:
            someones_score += score
    else:
        print('Invalid input')
