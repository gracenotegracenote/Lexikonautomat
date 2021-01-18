from __future__ import annotations

import os
from typing import List

import graphviz

from state import State


class LexAutomaton:
    def __init__(self):
        """
        Constructor of lexical automaton.
        """
        # init root state
        self.trie = State(False)

        # init register which saves states by hash value
        self.register = {self.trie}

    def build(self, words: List[str]) -> LexAutomaton:
        # add words to the automaton
        previous_word = ''
        for current_word in words:
            common_prefix = self.get_common_prefix(current_word, previous_word)
            last_state = self.get_last_state(common_prefix)
            current_suffix = self.get_current_suffix(current_word, common_prefix)
            if last_state.has_children():
                self.replace_or_register(last_state)
            self.add_suffix(last_state, current_suffix)
            previous_word = current_word

        self.replace_or_register(self.trie)

        return self

    def word_exists(self, word: str) -> bool:
        """
        Searches provided word in the lexical automaton.
        :param word: word to search for
        :return: true if the word could be found
        """
        current_state = self.trie
        for i in range(len(word)):
            symbol = word[i]
            if symbol not in current_state.children:
                return False

            current_state = current_state.children[symbol]

            if i == len(word) - 1 and not current_state.final:
                return False

        return True

    def get_language(self, state: State = None, words: List[str] = None, current_word: str = ''):
        """
        Searches for all words coded in the lexical automaton.
        :param state: state to begin the search from
        :param words: words already found
        :param current_word: current word (needed as variable while searching)
        :return: list of words
        """
        if words is None:
            words = set()
        if state is None:
            state = self.trie
        char_index = 0
        for symbol in state.children:
            if char_index != 0:
                current_word = current_word[0: len(current_word) - 1]
            current_word += symbol
            child = state.children[symbol]
            char_index += 1
            if child.final:
                words.add(current_word)
            if len(child.children) == 0:
                current_word = ''
            words = self.get_language(child, words, current_word)
        return words

    def draw(self, file_path):
        """
        Creates a graph from the lexical automaton and saves it in PDF format.
        :param file_path: file path of file to save graph in
        :return: None
        """
        dot = graphviz.Digraph(comment='LexAutomat')

        states, edges = self.get_states_and_edges()

        for state in states:
            if state.final:
                dot.node(str(state), label='', style='filled', color='blue')
            else:
                dot.node(str(state), label='')

        for parent, symbol, child in edges:
            dot.edge(str(parent), str(child), symbol)

        dot.render(file_path, view=True)

    def add_word(self, word, prev_word: str = None, online: bool = True):
        """
        Adds one word to the lexical automaton.
        :param word: word to add
        :param prev_word: word which was added previously (needed when adding words "offline")
        :param online: true when adding words "online"
        :return: None
        """
        print("New word added.")

    def remove_word(self, word: str) -> None:
        """
        Removes provided word from the lexical automaton.
        :param word: word to remove
        :return: None
        """
        print("Word removed.")

    def are_equivalent(self, state1: State, state2: State) -> bool:
        """
        State p belongs to the same class as q if and only if:
        1. they are either both final or both nonfinal; and
        2. they have the same number of outgoing transitions; and
        3. corresponding outgoing transitions have the same labels; and
        4. corresponding outgoing transitions lead to states that have the same right languages.
        (c) page 7

        :param state1:
        :param state2:
        :return:
        """

        # 1.
        if state1.final != state2.final:
            return False

        # 2.
        if len(state1.children) != len(state2.children):
            return False

        for label in state1.children:
            # 3.
            if label not in state2.children:
                return False

            # 4.
            if self.get_right_languages(state1) != self.get_right_languages(state2):
                return False

        return True

    def get_common_prefix(self, current_word, previus_word) -> str:
        return os.path.commonprefix([current_word, previus_word])

    def get_last_state(self, common_prefix: str) -> State:
        last_state = self.trie
        for label in common_prefix:
            last_state = last_state.children[label]
        return last_state

    def get_current_suffix(self, current_word: str, common_prefix: str) -> str:
        return current_word[len(common_prefix): len(current_word)]

    def replace_or_register(self, state: State) -> None:
        label, child = self.get_last_child(state)
        if child.has_children():
            self.replace_or_register(child)

        for registered_state in self.register:
            if self.are_equivalent(registered_state, child):
                state.children[label] = registered_state
                return

        self.register.add(child)

    def add_suffix(self, state: State, suffix: str) -> None:
        current_state = state
        for i in range(len(suffix)):
            child = State(i == len(suffix) - 1)
            current_state.add_child(child, suffix[i])
            current_state = child

    def get_last_child(self, state: State) -> [str, State]:
        label = list(state.children.keys())[-1]
        child = state.children[label]
        return label, child

    def is_in_register(self, child: State) -> State:
        print("Getting state from register.")
        return State(True)

    def get_right_languages(self, state: State) -> List[str]:
        return self.get_language(state=state)

    """
    def get_states_and_edges(self, state=None, states=None, edges=None):
        if state is None:
            state = self.trie
        if states is None:
            states = []
        if edges is None:
            edges = []

        if state in states:
            return states, edges
        states.append(state)
        for symbol in state.children:
            child = state.children[symbol]
            edges.append((state, symbol, child))
            if child not in states:
                states, edges = self.get_states_and_edges(state=child, states=states, edges=edges)

        return states, edges
    """

    def get_states_and_edges(self):
        """
        Searches all states and edges of the lexical automaton.
        :param state: state to begin with
        :param states: states found already
        :param edges: edges found already
        :return: list of states and list of edges
        """
        states = []
        edges = []

        for state in self.register:
            states.append(state)
            for label in state.children:
                edges.append((state, label, state.children[label]))

        return states, edges
