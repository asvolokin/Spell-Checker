from itertools import permutations

class Checker:
    def __init__(self, dictionary, wrong_words):
        self.dictionary = dictionary
        self.wrong_words = wrong_words

    def permutations_of_word(self):
        poss = []
        sugg = []
        perm = permutations(self.wrong_words)
        for items in list(perm):
            poss.append(items)

        possibilities = []

        for elements in poss:
            attempts = ''
            for items in elements:
                attempts += items
            possibilities.append(attempts)

        for items in possibilities:
            if items in self.dictionary and items not in sugg:
                sugg.append(items)

        return sugg

    def double_to_single_letters(self):
        sugg = []
        poss = []

        element = list(self.wrong_words)
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
            if items in self.dictionary and items not in sugg:
                sugg.append(items)

        return sugg

    def single_letters_to_double_letters(self):
        sugg = []
        poss = []
        element = str(self.wrong_words)
        for i in range(len(element) - 1):
            possibility = element[:i] + element[i] + element[i:]
            poss.append(possibility)

        for items in poss:
            if items in self.dictionary and items not in sugg:
                sugg.append(items)

        return sugg

    def remove_first_letter(self):
        sugg = []
        element = str(self.wrong_words)
        if element[1:] in self.dictionary:
            sugg.append(element[1:])

        return sugg

    def remove_last_letter(self):
        sugg = []
        element = str(self.wrong_words)
        if element[:-1] in self.dictionary:
            sugg.append(element[:-1])

        return sugg
