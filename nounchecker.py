class NounChecker:
    def __init__(self, errors, noun):
        """
        The function that defines the objects for this class
        :param errors: The list of words spelled incorrectly
        :param noun: The list of all nouns in the English Language
        """
        self._errors = errors
        self._noun = noun

    def possessive_nouns(self):
        """
        A method that tests if a word is a possessive noun and removes it from the wrong word list if was placed
        into that list
        :return: Nothing
        """
        r = r"'s"
        for word in self._errors:
            if r in word:
                k = word.replace(r, '')
                # removes the 's to test if the word is a noun
                if k in self._noun:
                    self._errors.remove(word)
                # if the word without the possessive part is a noun, then it is removed from the wrong word list

    def plural_possessive_nouns(self):
        """
        A method that tests if a word is a plural possessive noun and removes it from the wrong word list if was
        placed into that list
        :return: Nothing
        """
        r = r"s'"
        for word in self._errors:
            if r in word:
                k = word.replace(r, '')
                # removes the s' to test if the word is a noun
                if k in self._noun:
                    self._errors.remove(word)
                # if the word without the plural possessive part is a noun, then it is removed from the wrong word list
