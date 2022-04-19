import time
from checker import Checker
from wordlists import WordLists

tic = time.perf_counter()
dictionary = {}


def text(f):
    f = open(f, encoding='utf8')
    contents = f.read()
    f.close()
    spelling_errors = []
    contents = contents.lower()
    WordLists.dictionary(dictionary)
    for p in """,.<>?/;:"[]{}|=_+)(*&^%$#@!`~""":  # gets rid of all punctuation
        contents = contents.replace(p, '')
    contents = contents.split()
    for word in contents:
        if word in dictionary:
            continue
        else:
            spelling_errors.append(word)
    Checker.possessive_nouns(spelling_errors)
    Checker.plural_possessive_nouns(spelling_errors)
    return spelling_errors


toc = time.perf_counter()

print(toc-tic)
print(text('test.txt'))
