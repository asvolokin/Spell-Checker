from itertools import permutations


class Checker:
    def __init__(self, dictionary, wrong_words):
        """
        A function to create an object that will produce suggestions for the wrong words
        :param dictionary: The dictionary of all possible English words
        :param wrong_words: Takes the wrong words that are found from the text file
        """
        self._dictionary = dictionary
        self._wrong_words = wrong_words

    def permutations_of_word(self):
        """
        A function that checks all permutations of a word to see if they are possible suggestions
        :return: all permutations that are in the dictionary
        """
        poss = []
        sugg = []
        perm = permutations(self._wrong_words)
        for items in list(perm):
            poss.append(items)  # appends all permutations to a list

        possibilities = []

        for elements in poss:
            attempts = ''
            for items in elements:
                attempts += items
            possibilities.append(attempts)
        # Loops that turn every item in the list of permutations into a list of strings

        for items in possibilities:
            if items in self._dictionary and items not in sugg:
                sugg.append(items)
            # appends the words to the suggestion list if they are in the dictionary

        return sugg  # returns the list of suggestions

    def double_to_single_letters(self):
        """
        A method that returns suggestions that eliminates double letters
        :return: suggestion list for double-to-single letter transformations that are in the dictionary
        """
        sugg = []
        poss = []

        element = list(self._wrong_words)
        for i in range(len(element)-1):
            if element[i - 1] == element[i - 2]:
                del element[i - 1]
                poss.append(element)
        # appends a word to list of possibilities if there are letters doubled

        possibilities = []

        for elements in poss:
            attempts = ''
            for items in elements:
                attempts += items
            possibilities.append(attempts)
        # turns the list of possibilities into strings to be tested

        for items in possibilities:
            if items in self._dictionary and items not in sugg:
                sugg.append(items)
            #  appends the items to suggestion list if they are in the dictionary

        return sugg  # returns the list of suggested words

    def single_letters_to_double_letters(self):
        """
        A method that tests all letters for single letters turning into double letters
        :return: suggestion list containing all words in the dictionary that contain the single to double letter
        transformations for the wrong word
        """
        sugg = []
        poss = []
        element = str(self._wrong_words)
        for i in range(len(element) - 1):
            possibility = element[:i] + element[i] + element[i:]
            poss.append(possibility)
        # for every letter, a possibility is appended to the list where that letter is doubled

        for items in poss:
            if items in self._dictionary and items not in sugg:
                sugg.append(items)
            # appends all the possibilities that are in the dictionary to a list of suggestions

        return sugg  # returns the list of suggestions

    def remove_first_letter(self):
        """
        A method that tests if removing the first letter creates a possible word replacement
        :return: a list containing a suggestion if the removing the first letter produces a word in the dictionary
        or an empty list if it does not
        """
        sugg = []
        element = str(self._wrong_words)
        if element[1:] in self._dictionary:
            sugg.append(element[1:])
        # appends the item to a suggestion list if when the first letter is removed, the word is in the dictionary

        return sugg  # returns the suggestion list

    def remove_last_letter(self):
        """
        A method that tests if removing the last letter creates a possible word replacement
        :return: a list containing a suggestion if the removing the last letter produces a word in the dictionary
        or an empty list if it does not
        """
        sugg = []
        element = str(self._wrong_words)
        if element[:-1] in self._dictionary:
            sugg.append(element[:-1])
        # appends the word to a suggestion list if the word is in the dictionary when the last letter is removed

        return sugg  # returns the list of suggested words
