class FixWords:
    @staticmethod
    def fix_text(wrong_words, suggestions, original, index, loop):
        """
        A method that will fix the text file
        :param wrong_words: The list of wrong words
        :param suggestions: The combination of all suggested words
        :param original: The original text file
        :param index: The index that a user is selecting to replace the
        :param loop: Keeps track of the number of times the loop has been run through
        :return: The updated text file
        """
        file = True
        while file:
            if index > len(suggestions) - 1:
                index = int(input('Invalid index, please try again: ')) - 1
                # If the user selects an index greater than the number of suggestions, have them input it again
            elif suggestions[index] == 'None of these options':
                return original
                # If they select the index that corresponds to None of these options return the original spelling
            elif index < len(suggestions) - 1:
                original = original.replace(wrong_words[loop], suggestions[index])
                # If the user selects an index, replace the wrong word with the suggestion at that index
                file = False

        return original
