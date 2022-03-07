from math import ceil


def is_palindrome_recursive(word, low_index, high_index):

    if len(word) == 0:
        return False

    if low_index == ceil(len(word) / 2) or 0 < len(word) <= 2:
        return True

    while low_index < ceil(len(word) / 2):
        if word[low_index] == word[high_index]:
            # limit_iteractions = limit_iteractions + 1
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        else:
            return False
