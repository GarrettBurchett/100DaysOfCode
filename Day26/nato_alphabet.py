import pandas as pd

phonetic_alphabet = pd.read_csv("Day26/nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for index, row in phonetic_alphabet.iterrows()}

def generate_phonetic_word():
    word = input("Enter a word: ").upper()
    try:
        result = [alphabet_dict[letter] for letter in word] # if letter.isalpha()
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic_word()
    else:    
        print(result)

generate_phonetic_word()