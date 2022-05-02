class WordLists:
    @staticmethod
    def dictionary(dictionary):
        """
        A function that creates a dictionary that has every word in the dictionary
        :param dictionary: an empty dictionary
        :return: The dictionary of all words
        """
        with open('dictionary.txt') as dic:
            for words in dic:
                words = words.strip().lower()
                # standardizes the words in the dictionary
                dictionary[words] = words
                # puts all words from the dictionary in the dictionary

    @staticmethod
    def nouns(nouns):
        """
        A function that creates a dictionary that contains every noun in the English Language
        :param nouns: an empty dictionary
        :return: A dictionary of all nouns in it
        """
        with open('nouns.txt') as noun:
            for words in noun:
                words = words.strip().lower()
                # standardizes the words in the nouns list
                nouns[words] = words
                # puts all nouns in the nouns dictionary
