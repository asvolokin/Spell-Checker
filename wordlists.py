class WordLists:
    @staticmethod
    def dictionary(dictionary):
        with open('dictionary.txt') as dic:
            for words in dic:
                words = words.strip().lower()
                dictionary[words] = words

    @staticmethod
    def nouns(nouns):
        with open('nouns.txt') as noun:
            for words in noun:
                words = words.strip().lower()
                nouns[words] = words
