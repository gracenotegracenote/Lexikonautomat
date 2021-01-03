from unittest import TestCase

from lex_automaton import LexAutomaton
from state import State


class TestLexAutomaton(TestCase):
    def setUp(self):
        self.fillLexAutomaton()

    def test_word_exists(self):
        self.assertTrue(self.automaton.word_exists('kater'))

    def test_word_not_exists(self):
        self.assertFalse(self.automaton.word_exists('uni'))

    def test_get_language(self):
        self.assertCountEqual(self.automaton.get_language(), self.language)

    # def test_draw(self):
        # self.automaton.draw('test_draw_automaton.gv')

    """
    def test_add_word(self):
        self.fail()

    def test_remove_word(self):
        self.fail()

    def test_are_equivalent(self):
        self.fail()
    """

    def test_get_common_prefix(self):
        current_word = 'kater'
        previous_word = 'katze'
        self.assertEqual(self.automaton.get_common_prefix(current_word, previous_word), 'kat')

    def test_get_last_state(self):
        self.assertEqual(self.automaton.get_last_state('kat'), self.states[4])

    def test_get_current_suffix(self):
        current_word = 'kater'
        common_prefix = 'kat'
        self.assertEqual(self.automaton.get_current_suffix(current_word, common_prefix), 'er')

    """
    def test_replace_or_register(self):
        self.fail()

    def test_add_suffix(self):
        self.fail()
    """

    def test_get_states_and_edges(self):
        states, edges = self.automaton.get_states_and_edges()
        self.assertCountEqual(states, self.states)
        self.assertCountEqual(edges, self.edges)

    def fillLexAutomaton(self):
        self.automaton = LexAutomaton()

        last = State(True)
        first = State(False)

        # add words Kater und Katze
        state4 = State(False)
        state4.children['r'] = last
        state5 = State(False)
        state5.children['e'] = last
        state3 = State(False)
        state3.children['e'] = state4
        state3.children['z'] = state5
        state2 = State(False)
        state2.children['t'] = state3
        state1 = State(False)
        state1.children['a'] = state2
        first.children['k'] = state1

        self.automaton.trie = first

        self.states = [first, last, state1, state2, state3, state4, state5]
        self.edges = [(first, 'k', state1), (state1, 'a', state2), (state2, 't', state3), (state3, 'e', state4),
                      (state3, 'z', state5), (state4, 'r', last), (state5, 'e', last)]

        self.language = ['kater', 'katze']
