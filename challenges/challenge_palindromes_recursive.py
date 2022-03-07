from math import ceil


def is_palindrome_recursive(word, low_index, high_index):

    # limit_iteractions = 0

    if low_index == ceil(len(word) / 2) or len(word) <= 2:
        return True

    while low_index < ceil(len(word) / 2):
        # equality = word[low_index] == word[high_index]

        # if len(word) <= 2:
        #     limit_iteractions = limit_iteractions + 1
        #     return is_palindrome_recursive(word, low_index, high_index)
        # print(limit_iteractions)
        if word[low_index] == word[high_index]:
            # limit_iteractions = limit_iteractions + 1
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        else:
            return False
