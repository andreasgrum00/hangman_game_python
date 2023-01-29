from hangman import choose_pics as cp
from words import choose_random_word as cw
from os import system

system("cls")

word = cw()

game_is_over = False
mistakes = 0
state = 1
correct_letters = []

while not game_is_over:
    print(cp(state))
    for letter in word:
        if(letter in correct_letters):
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

    guess = str(input(f"\nMistakes: {mistakes}\nYour guess (Word or letter): "))

    if(guess in word):
        system('cls')
        print("Correct!")
        correct_letters.append(guess.lower())

        if((guess == word) or (set(correct_letters) == set(word))):
            print("You just won! Congrats *clap clap*")
            break
        continue
    else:
        system('cls')
        print("It is not correct... Try again!")
        mistakes += 1
        state += 1

        if(mistakes >= 6):
            print("Ya died :(")
            game_is_over = True
            break
        continue