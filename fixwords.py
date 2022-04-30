class FixWords:
    @staticmethod
    def fix_text(wrong_words, suggestions, original, index, loop):
        file = True
        while file:
            if index > len(suggestions) - 1:
                index = int(input('Invalid index, please try again: ')) - 1
            elif suggestions[index] == 'None of these options':
                return original
            elif index < len(suggestions) - 1:
                original = original.replace(wrong_words[loop], suggestions[index])
                file = False

        return original
