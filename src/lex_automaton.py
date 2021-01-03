from __future__ import annotations

import os
from typing import List

from state import State


class LexAutomaton:
    def __init__(self):
        """
        Constructor of lexical automaton.
        """
        # init register which saves states by hash value
        self.register = {}

        # init root state
        self.trie = State(False)

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

    def word_exists(self, word: str):
        """
        Searches provided word in the lexical automaton.
        :param word: word to search for
        :return: true if the word could be found
        """
        return False

    def get_language(self, state: State = None, words: List[str] = None, current_word: str = ''):
        """
        Searches for all words coded in the lexical automaton.
        :param state: state to begin the search from
        :param words: words already found
        :param current_word: current word (needed as variable while searching)
        :return: list of words
        """
        return []

    def draw(self, file_path: str):
        """
        Creates a graph from the lexical automaton and saves it in PDF format.
        :param file_path: file path of file to save graph in
        :return: None
        """
        print("Graph created.")

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
        return False

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
        child = self.get_last_child(state)
        if child.has_children():
            self.replace_or_register(child)
        if self.get_from_register(child):
            self.set_last_child(state, child)
            self.delete(child)
        else:
            self.add_to_register(child)

    def add_suffix(self, last_state: State, current_suffix: str) -> None:
        print("Add suffix.")

    def get_last_child(self, state: State) -> State:
        print("Getting last child.")
        return State(True)

    def get_from_register(self, child: State) -> State:
        print("Getting state from register.")
        return State(True)

    def set_last_child(self, state: State, last_child: State) -> None:
        print("Setting last child.")

    def delete(self, state: State) -> None:
        print("Deleting state.")

    def add_to_register(self, child: State) -> None:
        print("Adding to register.")
