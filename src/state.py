class State:
    def __init__(self, final):
        """
        Construtor of state.
        :param final: true if state is final
        :param children: list of children
        """
        self.final = final
        self.children = {}
        self.parents = []
        self.hash_value = ''
        self.string_value = ''

    def has_children(self):
        return bool(self.children)

    def add_child(self, child, label):
        """
        Adds child to the state.
        :param child: child to add
        :param label: symbol to add
        :return: None
        """
        self.children[label] = child
        child.parents.append(self)

    def hash(self, hashed_states=None):
        """
        Calculates hash value of the state and its children.
        :param hashed_states: states calculated already
        :return: hash value
        """
        if hashed_states is None:
            hashed_states = []
        hashed_states.append(self)

        result = '1' if self.final else '0'
        result += str(len(self.children))
        for symbol in self.children:
            child = self.children[symbol]
            if child in hashed_states:
                result += str(symbol) + child.hash_value
            else:
                result += str(symbol) + self.children[symbol].hash(hashed_states)

        self.hash_value = result
        return result

    def copy(self):
        """
        Copies state and its children. Ignores parents.
        :return: a copy of provided state and its children
        """
        new_state = State(self.final)
        for symbol in self.children:
            child = self.children[symbol]
            new_state.add_child(child.copy(), symbol)
        return new_state
