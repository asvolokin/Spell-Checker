class NounChecker:
    def __init__(self, errors, noun):
        self.errors = errors
        self.noun = noun

    def possessive_nouns(self):
        r = r"'s"
        for word in self.errors:
            if r in word:
                k = word.replace(r, '')
                if k in self.noun:
                    self.errors.remove(word)

    def plural_possessive_nouns(self):
        r = r"s'"
        for word in self.errors:
            if r in word:
                k = word.replace(r, '')
                if k in self.noun:
                    self.errors.remove(word)
