# from math import ceil


def is_palindrome_iterative(word):
    min_index = 0
    max_index = len(word) - 1

    if len(word) == 0:
        return False

    while min_index < max_index:
        if word[min_index] != word[max_index]:
            return False
        min_index = min_index + 1
        max_index = max_index - 1
    return True
