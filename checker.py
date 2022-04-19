from wordlists import WordLists


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

