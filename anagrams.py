import random
import os

def wordPicker(filename):
    with open(filename) as handler:
        selected = [line for line in handler]
        return random.choice(selected)

def letterScrambler():
    while (1):
        index = random.randint(0, len(word)-1)
        if (index not in shown and len(shown) != len(word)):
            shown.append(index)
            print(word[index], " ", end = "")
        if (len(shown) == len(word)):
            shown.clear()
            break

if __name__ == "__main__":
    print("Welcome to Anagrams! Press 1 for a random word, or press 2 for a custom word")
    option = input()
    word = ""
    if int(option) == 1:
        word = wordPicker("10000words.txt")
        # print(word)
        word = word[:-1]
        while (len(word) < 4):
            word = wordPicker("10000words.txt")
            word = word[:-1]
            # print(word)
    elif int(option) == 2:
        word = input("Go ahead and type in the custom word: ")
        clear = lambda: os.system('cls')
        clear()
    print("*Note: Words can be proper nouns, but all letters will be in lowercase")
    print("To rescramble the letters, press space then enter")
    print("Your letters are the following:")
    guessed = len(word)*[0]
    shown = []
    letterScrambler()
    print("\n")
    for a in range(len(word) + 6):
        if (a == len(word) + 5):
            print("Oh no, no more guesses left! The word was " + word)
            break
        guess = input("Enter a word to guess: ")
        if (word == guess):
            print("Congratulations, you guessed the word!")
            break
        if (guess == " "):
            letterScrambler()
            print("\n")
        elif (word != guess):
            print(guess + " is not the word, keep on guessing!")
    print("\n")
    input("Press enter to exit...")