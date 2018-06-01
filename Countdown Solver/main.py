from random import randint
import itertools
import ctypes

def load_words():
    with open('words.txt') as word_file:
        valid_words = list(word_file.read().split())
    return valid_words

def load_consonants():
    with open('consonants.txt') as consonants_file:
        valid_consonants = list(consonants_file.read().split())
    return valid_consonants

def load_vowels():
    with open('vowels.txt') as vowels_file:
        valid_vowels = list(vowels_file.read().split())
    return valid_vowels

if __name__ == '__main__':
    ctypes.windll.kernel32.SetConsoleTitleW("Countdown Solver")
    english_words = load_words()
    consonants = load_consonants()
    vowels = load_vowels()
    selected_letters = []

    user_input = input("Please enter the string of characters seperated by a comma or leave empty to randomly generate: (a,b,c,d,e,f,g,h,i) ")
    selected_letters = user_input.split(',')

    if len(selected_letters) == 0:	
	    num_const = randint(4,7)
	    print(len(consonants))

	    for _ in range(0, num_const):
	        selected_letters.append(consonants[randint(0, len(consonants) - 1)])

	    for _ in range(0, 9 - num_const):
	        selected_letters.append(vowels[randint(0, len(vowels) - 1)])

    print('Selected Letters: ')
    print(selected_letters)

    for i in range(0, len(selected_letters) + 1):
        for subset in itertools.permutations(selected_letters, i):
            ctypes.windll.kernel32.SetConsoleTitleW(''.join(subset))
            if len(subset) >= 5:
                word = ''.join(subset)
                if word in english_words:
                    print(word)