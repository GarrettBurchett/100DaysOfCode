import random
from hangman_words import word_list
from hangman_art import stages, logo


chosen_word = random.choice(word_list)
end_of_game = False
lives = 6
print(logo)

display = ['_'] * len(chosen_word)
letters_guessed = []

while not end_of_game:
    guess = input("What letter would you like to guess?\n").lower()
    
    while guess in letters_guessed:
        print(f"You've already guessed {guess}. Please pick another letter")
        guess = input("What letter would you like to guess?\n").lower()
    
    letters_guessed.append(guess)
    
    for i, letter in enumerate(chosen_word):
        if guess == letter:
            display[i] = guess
    
    if guess not in display:
        print(f"Letter {guess} is not in the word.")
        lives -= 1
    
    if lives == 0:
        print("\nOut of lives. You Lose!")
        print(f"The answer was: {chosen_word}")
        end_of_game = True
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print(stages[lives])
    if '_' not in display:
        end_of_game = True
        print("You Win!!!")        