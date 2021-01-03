import os

import graphviz

import helper
from constants import INVALID_WORD_MESSAGE
from state import State


class LexAutomaton:
    def __init__(self, file_path):
        """
        Constructor of lexical automaton.
        :param file_path: file path of file containing words from which an automaton will be built.
        """
        # read words
        words = helper.get_words(file_path, '\n')

        # init root state
        self.trie = State(False)

        # init register which saves states by hash value
        self.register = {}

        # add words from file to the automaton
        self.add(words, False)

    def add(self, words, online=True):
        """
        Adds list of words to the lexical automaton.
        :param words: list of words to add
        :param online: true if adding words "online"
        :return: None
        """
        # sort words
        words.sort()

        # add words
        prev_word = ''
        for current_word in words:
            self.add_word(current_word, prev_word, online)
            prev_word = current_word

    def add_word(self, word, prev_word=None, online=True):
        """
        Adds one word to the lexical automaton.
        :param word: word to add
        :param prev_word: word which was added previously (needed when adding words "offline")
        :param online: true when adding words "online"
        :return: None
        """
        # validate word
        if not helper.is_valid(word):
            print(INVALID_WORD_MESSAGE % word)
            return

        # get prefix and suffix
        common_prefix = self.get_common_prefix(word, prev_word, online)
        suffix = helper.get_suffix(word, common_prefix)

        # if nothing to add, stop
        if len(suffix) == 0:
            return

        # get first state to add suffix to, its parent and the symbol between them
        current_state, parent_state, symbol = self.get_last_state(common_prefix)

        # add suffix
        self.add_suffix(current_state, parent_state, symbol, common_prefix, suffix)

        # update register
        self.register = helper.update_register(self.trie, self.register)

    def get_common_prefix(self, word, prev_word, online):
        """
        Searches for the common part of two words.
        :param word: current word
        :param prev_word: word added previously
        :param online: true when adding word "online"
        :return: common prefix of provided words
        """
        return self.get_coded_part(word) if online else os.path.commonprefix([prev_word, word])

    def get_last_state(self, string):
        """
        Searches for the last state in the trie for given string.
        :param string: string to search in the trie
        :return: last state found, its parent state and the symbol between them
        """
        parent_state = None
        current_state = self.trie
        symbol = ''
        for char in string:
            if char in current_state.children:
                parent_state = current_state
                current_state = current_state.children[char]
                symbol = char

        return current_state, parent_state, symbol

    def add_suffix(self, state, parent_state, prev_symbol, prefix, suffix):
        """
        Builds new states and adds to the provided state based on provided suffix.
        :param state: state to add new states to
        :param parent_state: parent state
        :param prev_symbol: symbol connecting state and its parent
        :param prefix: prefix which is already exists in the trie
        :param suffix: suffix for building new states
        :return:
        """
        original_state = state

        if parent_state is not None and len(state.parents) > 1:
            # copy state
            state = state.copy()

            # remove parents
            state.parents = []

            # connect parent and new child
            parent_state.add_child(state, prev_symbol)

            # go up and find state with multiple parents
            state_with_multiple_parents = state
            prefix_length = len(prefix)
            symbol_index = prefix_length
            while len(state_with_multiple_parents.parents) == 1:
                state_with_multiple_parents = state_with_multiple_parents.parents[0]
                symbol_index -= 1
                if len(state_with_multiple_parents.parents) > 1:
                    break

            if len(state_with_multiple_parents.parents) > 1:
                # copy state
                state_copy = state_with_multiple_parents.copy()

                # assign copy to parents with same symbol
                parent_symbol = prefix[symbol_index - 1]
                for parent in state_with_multiple_parents.parents:
                    if parent_symbol in parent.children:
                        parent.add_child(state_copy, parent_symbol)
                        break

                # go down to the original state
                while symbol_index < prefix_length:
                    symbol = prefix[symbol_index]
                    state_copy = state_copy.children[symbol] if symbol in state_copy.children else state_copy
                    symbol_index += 1
                state = state_copy

                # return to the original structure
                parent_state.add_child(original_state, prev_symbol)

        # build sub-trie
        suffix_length = len(suffix)
        state_copy = state.copy()
        temp_register = {}
        current_state = state_copy
        for symbol_index in range(suffix_length):
            symbol = suffix[symbol_index]
            final = (symbol_index == suffix_length - 1)
            current_state.add_child(State(final), symbol)
            temp_register[-1] = current_state.children[symbol]

            temp_register = helper.update_register(state_copy, temp_register)
            current_state = current_state.children[suffix[symbol_index]]

        # merge sub-trie
        current_state = state_copy
        for symbol_index in range(suffix_length):
            symbol = suffix[symbol_index]
            child = current_state.children[symbol]

            # find equivalent state
            if child.hash_value in self.register:
                equivalent = self.register[child.hash_value]
                if len(child.children) == len(equivalent.children):
                    equal = True
                    for s in child.children:
                        if s not in equivalent.children:
                            equal = False
                            break
                    if equal:
                        state.add_child(equivalent, symbol)
                        break

            # add new child
            state.add_child(State(child.final), symbol)

            # update register
            self.register[-1] = state.children[symbol]
            self.register = helper.update_register(self.trie, self.register)

            current_state = current_state.children[symbol]
            state = state.children[symbol]

        # replace new leafs with the end state
        if parent_state is not None:
            self.replace_leafs(parent_state)

    def replace_leafs(self, state):
        """
        Iterates through the given state and replace leafs with the end state.
        :param state: state to search leafs in
        :return: None
        """
        for symbol in state.children:
            child = state.children[symbol]
            if child.final and len(child.children) == 0:  # if leaf
                state.add_child(self.register['10'], symbol)
            else:
                self.replace_leafs(child)

    def get_states_and_edges(self, state=None, states=None, edges=None):
        """
        Searches all states and edges of the lexical automaton.
        :param state: state to begin with
        :param states: states found already
        :param edges: edges found already
        :return: list of states and list of edges
        """
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

    def get_word(self, word):
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

    def remove_word(self, word):
        """
        Removes provided word from the lexical automaton.
        :param word: word to remove
        :return: None
        """
        states_to_remove = [self.trie]
        last_parent = None
        last_symbol = None

        # go below
        current_state = self.trie
        for i in range(len(word) - 1):  # last state can be ignored
            symbol = word[i]
            if symbol in current_state.children:
                parent = current_state
                current_state = current_state.children[symbol]

                if current_state.final:
                    if len(current_state.children) > 0:
                        states_to_remove.clear()
                        last_parent = parent
                        last_symbol = symbol
                    else:
                        break

                states_to_remove.append(current_state)

        if current_state.final and len(current_state.children) > 0:
            current_state.final = False
            return

        i = len(word) - 1
        for state in reversed(states_to_remove):
            if len(state.children) > 1:
                symbol = word[i]
                state.children.pop(symbol)
                break
            i -= 1

        if last_parent is not None and last_symbol is not None:
            last_parent.add_child(self.register['10'], last_symbol)

        self.register = helper.update_register(self.trie, self.register)

        # iterate through word and find equivalents
        current_state = self.trie
        for i in range(len(word)):
            symbol = word[i]
            if symbol not in current_state.children:
                break

            parent = current_state
            current_state = current_state.children[symbol]

            # find equivalent state
            if current_state.hash_value in self.register:
                equivalent = self.register[current_state.hash_value]
                if len(current_state.children) == len(equivalent.children) and id(current_state) != id(equivalent):
                    equal = True
                    for s in current_state.children:
                        if s not in equivalent.children:
                            equal = False
                            break
                    if equal:
                        parent.add_child(equivalent, symbol)
                        break

    def get_coded_part(self, word):
        """
        Searches for the part of the word which is already coded in the trie (= prefix).
        :param word: word to search for
        :return: found prefix
        """
        prefix = ''
        current_state = self.trie
        for symbol in word:
            if symbol not in current_state.children:
                break
            prefix += symbol
            current_state = current_state.children[symbol]

        return prefix

    def get_language(self, state=None, words=None, current_word=''):
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
        i = 0
        for symbol in state.children:
            if i != 0:
                current_word = current_word[0: len(current_word) - 1]
            current_word += symbol
            child = state.children[symbol]
            i += 1
            if child.final:
                words.add(current_word)
            if len(child.children) == 0:
                current_word = ''
            words = self.get_language(child, words, current_word)
        return words
