from checker import Checker
from wordlists import WordLists

dictionary = {}


def Spell_Check(f):
    with open(f, encoding='utf8') as fi:
        contents = fi.read()
    spelling_errors = []
    orig_content = contents
    contents = contents.lower()
    print('Your original text is:\n', orig_content)
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
    loop_num = 0
    for word in spelling_errors:
        print('\nThe word', word, 'is spelled incorrectly\n')
        lst1 = Checker.permutations_of_word(word)
        lst2 = Checker.double_to_single_letters(word)
        lst3 = Checker.single_letters_to_double_letters(word)
        total_sugg = [*lst1, *lst2, *lst3, "None of these options"]
        print(total_sugg)
        ind = int(input('Please indicate the word you would like to replace the original '
                      'with by the number position in the list: ')) - 1
        orig_content = Checker.fix_text(spelling_errors, total_sugg, orig_content, ind, loop_num)
        loop_num += 1
    with open(f, 'w+', encoding='utf8') as fi:
        fi.write(orig_content)
    print('\nThe final text in your file is:\n',orig_content)
    return


print(Spell_Check('test.txt'))
