import constants as c
from lex_automaton import LexAutomaton
import helper

# read words and sort them lexicographically
words = helper.read_words_from_file(c.WORD_LIST_PATH, '\n')
words.sort()

# build lexicon automaton
automaton = LexAutomaton().build(words)


def main_menu():
    """
    Prints main options in the console.
    :return: None
    """
    option = input(c.MAIN_MENU)

    while option not in c.ALL_OPTIONS:
        option = input(c.INVALID_INPUT_MESSAGE)

    if option == c.OPTION_0:
        exit(0)

    if option == c.OPTION_1:
        word = input(c.SEARCH_WORD_MESSAGE)
        word_search_option(word)
        return

    if option == c.OPTION_2:
        get_language_option()
        return

    if option == c.OPTION_3:
        draw_automaton_option()
        return

    if option == c.OPTION_4:
        word = input(c.ADD_WORD_MESSAGE)
        add_word_option(word)
        return

    if option == c.OPTION_5:
        word = input(c.REMOVE_WORD_MESSAGE)
        remove_word_option(word)
        return


def word_search_option(word):
    """
    Prints word search option in the console.
    :param word: word to search for
    :return: None
    """
    print(c.SEARCH_IN_PROGRESS_MESSAGE % word)
    exists = automaton.word_exists(word)
    message = c.WORD_FOUND_MESSAGE % word if exists \
        else c.WORD_NOT_FOUND_MESSAGE % word
    print(message)
    new_word = input(c.SEARCH_AGAIN_MESSAGE)
    if new_word == c.OPTION_0:
        main_menu()
    else:
        word_search_option(new_word)


def get_language_option():
    """
    Prints get language option in the console.
    :return: None
    """
    words = sorted(automaton.get_language())
    print(c.AUTOMATON_LANGUAGE_MESSAGE)
    for word in words:
        print(word)
    main_menu()


def draw_automaton_option():
    """
    Prints draw automaton option in the console.
    :return: None
    """
    print(c.DRAW_IN_PROGRESS_MESSAGE)
    automaton.draw(c.DRAW_FILE_PATH)
    print(c.DRAW_FINISHED_MESSAGE % (c.DRAW_FILE_PATH, c.DRAW_FILE_PATH))
    main_menu()


def add_word_option(word):
    """
    Prints add word option in the console.
    :param word: word to add
    :return: None
    """
    exists = automaton.word_exists(word)
    if exists:
        new_word = input(c.CANNOT_ADD_WORD_MESSAGE % word)
        if new_word == c.OPTION_0:
            main_menu()
        else:
            add_word_option(new_word)
    else:
        print(c.ADD_IN_PROGRESS_MESSAGE % word)
    automaton.add_word(word, '', True)
    print(c.WORD_ADDED_MESSAGE % word)
    new_word = input(c.ADD_AGAIN_MESSAGE)
    if new_word == '0':
        main_menu()
    else:
        add_word_option(new_word)


def remove_word_option(word):
    """
    Prints remove word option in the console.
    :param word: word to remove
    :return: None
    """
    exists = automaton.word_exists(word)
    if not exists:
        new_word = input(c.CANNOT_REMOVE_WORD_MESSAGE % word)
        if new_word == c.OPTION_0:
            main_menu()
        else:
            remove_word_option(new_word)
    else:
        print(c.REMOVE_IN_PROGRESS_MESSAGE % word)
        automaton.remove_word(word)
        print(c.WORD_REMOVED_MESSAGE % word)

    new_word = input(c.REMOVE_AGAIN_MESSAGE)
    if new_word == c.OPTION_0:
        main_menu()
    else:
        remove_word_option(new_word)


# call main menu
main_menu()
