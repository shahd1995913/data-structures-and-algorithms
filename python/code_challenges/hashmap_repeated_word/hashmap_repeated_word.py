"""
Write a function called repeated word that

finds the first word to occur more than once in a string

Arguments: string

Return: string

"""

from collections import defaultdict

def repeated_word(text_input):

    occur_word = defaultdict(lambda: 0)

    for obj in text_input.split():

        occur_word[obj] += 1

        if occur_word[obj] > 1:

            return obj
