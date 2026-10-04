import random 
from hangman_words import word_list 
from hangman_art import logo , stages 
print(logo)

lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)
display =""
for i in range(len(chosen_word)):
    display = display + "_ "

print(f"The word is {display} ")

print(f"******************* You have {lives} / 6 lives *********************")


guessed_letters=[]

game_over = False
while not game_over :
    guess = input("Guess a letter : ").lower()

    display = ""
    for letter in chosen_word:
        if letter == guess :
            display = display + letter 
            guessed_letters.append(letter)
        elif letter in guessed_letters :
            display = display + letter 
        else :
            display = display + "_"

    if guess not in chosen_word:
        lives = lives - 1 
    print(display)

    if "_"not in display :
        game_over = True 
        print("Game Over !! ")
