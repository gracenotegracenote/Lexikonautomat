import constants as c
import helper
from lex_automaton import LexAutomaton

automaton = LexAutomaton()


def start_question_menu():
    start_question = input("Moechtest du den Lexikonautomaten (1) aus der Wortliste erstellen oder (2) "
                           "aus der Datei laden?\n Bitte \"1\" oder \"2\" eingeben. >>> ")
    while start_question not in ["1", "2"]:
        start_question = input("Falsches Input. Das Programm wird beendet.")
        exit(0)

    if start_question == '1':
        # read words and sort them lexicographically
        words = helper.read_words_from_file(c.WORD_LIST_PATH_4, '\n')
        words.sort()

        # build lexicon automaton
        automaton.build(words)
        print("Der Lexikonautomat wurde aus der Wortliste erfolgreich geladen.")
    else:
        load_automaton_option()

    main_menu()


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
        save_automaton_option()
        return

    if option == c.OPTION_5:
        load_automaton_option()
        return


def word_search_option(word):
    """
    Prints word search option in the console.
    :param word: word to search for
    :return: None
    """
    print(c.SEARCH_IN_PROGRESS_MESSAGE % word)
    exists = automaton.word_exists(word)
    message = c.WORD_FOUND_MESSAGE % word if exists else c.WORD_NOT_FOUND_MESSAGE % word
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


def save_automaton_option():
    """
    Prints draw automaton option in the console.
    :return: None
    """
    print(c.SAVING_IN_PROGRESS_MESSAGE)
    automaton.save(c.SAVE_FILE_PATH)
    print(c.SAVING_FINISHED_MESSAGE)
    main_menu()


def load_automaton_option():
    """
    Prints draw automaton option in the console.
    :return: None
    """
    print(c.LOADING_IN_PROGRESS_MESSAGE)
    automaton.load(c.SAVE_FILE_PATH)
    print(c.LOADING_FINISHED_MESSAGE)
    main_menu()


# call menu
start_question_menu()
