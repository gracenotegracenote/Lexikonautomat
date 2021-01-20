WORD_LIST_PATH_1 = 'wordlists/wordlist.txt'
WORD_LIST_PATH_2 = 'wordlists/wordlist_100.txt'
WORD_LIST_PATH_3 = 'wordlists/wordlist_p227.txt'
WORD_LIST_PATH_4 = 'wordlists/wordlist_test.txt'

MAIN_MENU = 'Was moechtest du tun?\n' \
            '   (1) Wort abfragen\n' \
            '   (2) Automatensprache anzeigen\n' \
            '   (3) Automaten zeichnen\n' \
            '   (4) Automaten speichern\n' \
            '   (5) Automaten aus der Datei laden\n' \
            '   (0) Abbrechen\n' \
            'Bitte eingeben >>> '

OPTION_0 = '0'
OPTION_1 = '1'
OPTION_2 = '2'
OPTION_3 = '3'
OPTION_4 = '4'
OPTION_5 = '5'
ALL_OPTIONS = [OPTION_0, OPTION_1, OPTION_2, OPTION_3, OPTION_4, OPTION_5]

INVALID_INPUT_MESSAGE = 'Du kannst zwischen 1-5 waehlen. ' \
                        'Waehle noch einmal oder gebe 0 ein, um das Programm zu beenden. >>> '

INVALID_WORD_MESSAGE = 'Ungueltiges Wort: \"%s\" enthaelt ein Leerzeichen. Es kommt nicht in den Lexikonautomat.\n'

SEARCH_WORD_MESSAGE = 'Geben Sie das Wort ein, nach dem in dem Lexikonautomat gesucht werden soll >>> '

SEARCH_IN_PROGRESS_MESSAGE = 'Ich suche nach dem Wort \'%s\'...'

WORD_FOUND_MESSAGE = 'Das Wort \'%s\' konnte gefunden werden!'

WORD_NOT_FOUND_MESSAGE = 'Das Wort \'%s\' konnte nicht gefunden werden...'

SEARCH_AGAIN_MESSAGE = 'Moechtest du auf ein weiteres Wort suchen? (Waehle 0 um zu Hauptmenu zu gehen) >>> '

AUTOMATON_LANGUAGE_MESSAGE = 'Der Lexikonautomat besteht aus folgenden Woertern:'

DRAW_IN_PROGRESS_MESSAGE = 'Ich zeichne den Lexikonautomaten...'

DRAW_FILE_PATH = 'automaton.gv'

DRAW_FINISHED_MESSAGE = 'Fertig! Du findest die Zeichnung unter \'%s\' und \'%s.pdf\'.'

SAVE_FILE_PATH = 'saved_automaton.txt'

SAVING_IN_PROGRESS_MESSAGE = "Ich speichere den Lexikonautomaten nach \'%s\'..." % SAVE_FILE_PATH

SAVING_FINISHED_MESSAGE = "Fertig! Du findest den abgespeicherten Automaten unter \'%s\'." % SAVE_FILE_PATH

LOADING_IN_PROGRESS_MESSAGE = "Ich lade den Lexikonautomaten aus \'%s\'..." % SAVE_FILE_PATH

LOADING_FINISHED_MESSAGE = "Fertig! Der Automat wurde aus \'%s\' erfolgreich geladen." % SAVE_FILE_PATH
