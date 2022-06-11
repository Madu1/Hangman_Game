import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()  # letters that has been guessed by the user

    lives = 6
    # getting user input
    while len(word_letter) > 0 and lives > 0:
        # letters used
        # ' '.join('['a', 'b', 'cd']') --> 'a b cd'
        print('You have entered these letters: ', ' '.join(used_letter))

        # what current word is (ie W-R D)
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                lives = lives - 1  # take away a life if wrong
                print("Letter is not in word.")

        elif user_letter in used_letter:
            print("You have already used that letter. Please try again.")
        else:
            print("Invalid character. Please try again.   ")

    # get here when len(word_letter ==0  and liver s==0
    if lives == 0:
        print("You died, sorry, The word was", word)
    else:
        print("You guessed the word", word, '!!')


hangman()
