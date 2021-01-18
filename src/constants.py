WORD_LIST_PATH_1 = 'wordlists/wordlist.txt'
WORD_LIST_PATH_2 = 'wordlists/wordlist_100.txt'
WORD_LIST_PATH_3 = 'wordlists/wordlist_p227.txt'
WORD_LIST_PATH_4 = 'wordlists/wordlist_test.txt'

MAIN_MENU = 'Was moechtest du tun?\n' \
            '   (1) Wort abfragen\n' \
            '   (2) Automatensprache anzeigen\n' \
            '   (3) Automat zeichnen\n' \
            '   (4) Wort hinzufuegen\n' \
            '   (5) Wort loeschen\n' \
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

ADD_WORD_MESSAGE = 'Geben Sie das Wort ein, das in den Lexikonautomat hinzugefuegt werden soll >>> '

REMOVE_WORD_MESSAGE = 'Geben Sie das Wort ein, das aus dem Lexikonautomat geloescht werden soll >>> '

SEARCH_IN_PROGRESS_MESSAGE = 'Ich suche nach dem Wort \'%s\'...'

WORD_FOUND_MESSAGE = 'Das Wort \'%s\' konnte gefunden werden!'

WORD_NOT_FOUND_MESSAGE = 'Das Wort \'%s\' konnte nicht gefunden werden...'

SEARCH_AGAIN_MESSAGE = 'Moechtest du auf ein weiteres Wort suchen? (Waehle 0 um zu Hauptmenu zu gehen) >>> '

AUTOMATON_LANGUAGE_MESSAGE = 'Der Lexikonautomat besteht aus folgenden Woertern:'

DRAW_IN_PROGRESS_MESSAGE = 'Ich zeichne den Lexikonautomat...'

DRAW_FILE_PATH = 'automaton.gv'

DRAW_FINISHED_MESSAGE = 'Fertig! Du findest die Zeichnung unter %s und %s.pdf.'

CANNOT_ADD_WORD_MESSAGE = 'Das Wort \'%s\' ist in dem Lexikonautomat schon enthalten. ' \
                          'Waehle ein anderes Wort. (Waehle 0 um zu Hauptmenu zu gehen) >>> '

ADD_IN_PROGRESS_MESSAGE = 'Ich fuege das Wort \'%s\' zu dem Lexikonautomat hinzu...'

WORD_ADDED_MESSAGE = 'Das Wort \'%s\' ist erfolgreich hinzugefuegt!'

ADD_AGAIN_MESSAGE = 'Moechtest du ein weiteres Wort hinzufuegen? (Waehle 0 um zu Hauptmenu zu gehen) >>> '

CANNOT_REMOVE_WORD_MESSAGE = 'Das Wort \'%s\' ist nicht in dem Automat enthalten. Waehle ein anderes Wort >>> '

REMOVE_IN_PROGRESS_MESSAGE = 'Ich loesche das Wort \'%s\' aus dem Lexikonautomat...'

WORD_REMOVED_MESSAGE = 'Das Wort \'%s\' ist erfolgreich geloescht!'

REMOVE_AGAIN_MESSAGE = 'Moechtest du ein weiteres Wort loeschen? (Waehle 0 um zu Hauptmenu zu gehen) >>> '
