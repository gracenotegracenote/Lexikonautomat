from unittest import TestCase

from lex_automaton import LexAutomaton

# create lexicon automaton
automaton = LexAutomaton()


class TestLexAutomaton(TestCase):
    """
    def test_word_exists(self):
        self.assertTrue(automaton.word_exists('Kater'))

    def test_word_not_exists(self):
        self.assertFalse(automaton.word_exists('Uni'))

    def test_get_language(self):
        self.fail()

    def test_draw(self):
        self.fail()

    def test_add_word(self):
        self.fail()

    def test_remove_word(self):
        self.fail()

    def test_are_equivalent(self):
        self.fail()
    """

    def test_get_common_prefix(self):
        current_word = 'Kater'
        previus_word = 'Katze'
        self.assertEqual(automaton.get_common_prefix(current_word, previus_word), 'Kat')

    """
    def test_get_last_state(self):
        self.fail()
    """

    def test_get_current_suffix(self):
        current_word = 'Kater'
        common_prefix = 'Kat'
        self.assertEqual(automaton.get_current_suffix(current_word, common_prefix), 'er')

    """
    def test_replace_or_register(self):
        self.fail()

    def test_add_suffix(self):
        self.fail()
    """
