from wordlists import WordLists
from itertools import permutations
from fileinput import FileInput

class Checker:
    @staticmethod
    def possessive_nouns(f):
        noun = {}
        WordLists.nouns(noun)
        r = r"'s"
        for word in f:
            if r in word:
                k = word.replace(r, '')
                if k in noun:
                    f.remove(word)

    @staticmethod
    def plural_possessive_nouns(f):
        noun = {}
        WordLists.nouns(noun)
        r = r"s'"
        for word in f:
            if r in word:
                k = word.replace(r, '')
                if k in noun:
                    f.remove(word)

    @staticmethod
    def permutations_of_word(wrong_words):
        dictionary = {}
        WordLists.dictionary(dictionary)
        poss = []
        sugg = []
        perm = permutations(wrong_words)
        for items in list(perm):
            poss.append(items)

        possibilities = []

        for elements in poss:
            attempts = ''
            for items in elements:
                attempts += items
            possibilities.append(attempts)

        for items in possibilities:
            if items in dictionary and items not in sugg:
                sugg.append(items)

        return sugg

    @staticmethod
    def double_to_single_letters(wrong_words):
        dictionary = {}
        WordLists.dictionary(dictionary)
        sugg = []
        poss = []

        element = list(wrong_words)
        for i in range(len(element)-1):
            if element[i] == element[i - 1]:
                del element[i]
                poss.append(element)

        possibilities = []

        for elements in poss:
            attempts = ''
            for items in elements:
                attempts += items
            possibilities.append(attempts)

        for items in possibilities:
            if items in dictionary and items not in sugg:
                sugg.append(items)

        return sugg

    @staticmethod
    def single_letters_to_double_letters(wrong_words):
        dictionary = {}
        WordLists.dictionary(dictionary)
        sugg = []
        poss = []
        element = str(wrong_words)
        for i in range(len(element) - 1):
            possibility = element[:i] + element[i] + element[i:]
            poss.append(possibility)

        for items in poss:
            if items in dictionary and items not in sugg:
                sugg.append(items)

        return sugg

    @staticmethod
    def fix_text(wrong_words, suggestions, original, index, loop):
        file = True
        while file:

            if index > len(suggestions) -1:
                index = int(input('Invalid index, please try again'))
            elif suggestions[index] == 'None of these options':
                return original
            elif index < len(suggestions) -1:
                original = original.replace(wrong_words[loop], suggestions[index])
                file = False

        return original

