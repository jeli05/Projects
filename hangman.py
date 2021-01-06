import random
import os

def wordPicker(filename):
    with open(filename) as handler:
        selected = [line for line in handler]
        return random.choice(selected)

if __name__ == "__main__":
    print("Welcome to Hangman! Press 1 for a random word, or press 2 for a custom word")
    option = input()
    word = ""
    if int(option) == 1:
        word = wordPicker("10000words.txt")
        word = word[:-1]
    elif int(option) == 2:
        word = input("Go ahead and type in the custom word: ")
        clear = lambda: os.system('cls')
        clear()
    wordList = []
    print("*Note: Words can be proper nouns, but all words will be in lowercase")
    print("Your word to guess is " + str(len(word)) + " letters long!")
    guessed = len(word)*[0]
    for i in range(len(word)):
        print("_", " ", end = "")
        wordList.append(word[i])
    print("\n")
    for a in range(len(word) + 6):
        if (a == len(word) + 5):
            print("Oh no, no more guesses left! The word was " + word)
            break
        letter = input("Enter a lowercase letter to guess: ")
        if not letter.isalpha() or len(letter) != 1:
            print("You can only guess letters of the alphabet")
            continue
        elif letter.isupper():
            print("You must guess lowercase letters only")
            continue
        elif letter in guessed:
            print("You've already guessed this letter!")
            continue
        elif letter not in wordList:
            print(letter + " is not in the word, take another guess!")
            continue
        if letter in wordList:
            index = wordList.index(letter)
        for j in range(len(word)):
            if letter == wordList[j]:
                guessed[j] = letter
        for i in range(len(word)):
            if guessed[i] != 0:
                print(guessed[i], " ", end="")
            else:
                print("_", " ", end="")
        print("\n")
        if 0 not in guessed:
            print("Congratulations, you guessed the word!")
            break