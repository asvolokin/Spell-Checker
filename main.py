from checker import Checker
from wordlists import WordLists
from nounchecker import NounChecker
from fixwords import FixWords

file_name = input('Enter the name of the .txt file that you would like to run a spell check on: ')


def spell_check(f):  # spell check is the main function that runs each of the simpler tests
    with open(f, encoding='utf8') as fi:
        contents = fi.read()  # reads all the contents and creates a string to contain the file
    spelling_errors = []
    orig_content = contents
    # created a copy of the original contents before any operations are done to the string
    contents = contents.lower()
    print('Your original text is:\n', orig_content)
    dictionary = {}
    WordLists.dictionary(dictionary)
    nouns = {}
    WordLists.nouns(nouns)
    # calls a function that creates the dictionary within a dictionary
    for p in """,.<>?/;:"[]{}|=_+)(*&^%$#@!`~""":  # gets rid of all punctuation
        contents = contents.replace(p, '')
    contents = contents.split()
    # normalizes the contents to get it to a point that it can be checked in the dictionary
    for word in contents:
        if word in dictionary:
            continue
        else:
            spelling_errors.append(word)
    # puts all words not contained in a dictionary into a list
    noun_checks = NounChecker(spelling_errors, nouns)
    NounChecker.possessive_nouns(noun_checks)
    # removes any words from the spelling errors list if they are a possessive noun not contained in the dictionary
    NounChecker.plural_possessive_nouns(noun_checks)
    # removes any words from the spelling errors list if they are plural possessive nouns
    loop_num = 0
    for word in spelling_errors:
        item = Checker(dictionary, word)
        print('\nThe word', word, 'is spelled incorrectly\n')
        lst1 = Checker.permutations_of_word(item)
        # produces all possible replacement words from the permutation method
        lst2 = Checker.double_to_single_letters(item)
        # produces all possible replacement words from the double letter replacement method
        lst3 = Checker.single_letters_to_double_letters(item)
        # produces all possible replacement words from the sing letter replacement method
        lst4 = Checker.remove_first_letter(item)
        lst5 = Checker.remove_last_letter(item)
        total_sugg = [*lst1, *lst2, *lst3, *lst4, *lst5, "None of these options"]
        # concatenates the lists of all possible replacements into a single list to choose from
        print(total_sugg)
        ind = int(input('Please indicate the word you would like to replace the original '
                      'with by the number position in the list: ')) - 1
        # Allows users to pick which word they want to replace or if they want to at all
        orig_content = FixWords.fix_text(spelling_errors, total_sugg, orig_content, ind, loop_num)
        # fixes the text with the user inputs
        loop_num += 1
    with open(f, 'w+', encoding='utf8') as fi:
        fi.write(orig_content)
        # writes the new fixed text into the original file
    print ('\nThe final text in your file is:\n', orig_content)
    return ''


file_is_there = True
while file_is_there:  # runs a loop to have a user input a file name until they have a
    # matching txt file that the spell checker can run on
    try:
        print(spell_check(file_name))
        file_is_there = False
    except FileNotFoundError:
        file_name = input(print('This file does not exist, please input a new file name: '))
