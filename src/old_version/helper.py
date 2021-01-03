import re

REGEX = re.compile('[\n\t ]')


def get_words(file_path, split_by):
    """
    Reads words from file.
    :param file_path: file path of file to read from
    :param split_by: character that separates words in provided file
    :return: list of words
    """
    file = open(file_path, 'r', encoding='utf8')
    words = file.read().split(split_by)
    file.close()
    return words


def is_valid(word):
    """
    Checks if provided word is valid (= contains no empty characters).
    :param word: word to validate
    :return: true if word is valid
    """
    return REGEX.search(word) is None


def get_suffix(word, prefix):
    """
    Searches for the end part of a word.
    :param word: word to search in
    :param prefix: first part of the word to cut off
    :return: word suffix
    """
    return word[len(prefix): len(word)]


def update_register(trie, register):
    """
    Updates entries in register by recalculating hash values of the states saved in it.
    :param trie: state to begin with
    :param register: register to update
    :return: updated register
    """
    trie.hash()
    new_register = {}
    for hash_value in register:
        state = register[hash_value]
        new_register[state.hash_value] = state

    return new_register
