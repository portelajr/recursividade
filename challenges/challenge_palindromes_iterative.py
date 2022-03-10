# from math import ceil


def is_palindrome_iterative(word):
    min_index = 0
    max_index = len(word) - 1
    # print(min_index, max_index)
    # limit_iteractions = ceil(len(word) / 2)
    # print(limit_iteractions)

    while min_index < max_index:
        if word[min_index] != word[max_index]:
            return False
        min_index = min_index + 1
        max_index = max_index - 1
    return True


# print(is_palindrome_iterative("ANA"))

# def is_palindrome_recursive(word, low_index, high_index):

#     if len(word) == 0:
#         return False

#     if low_index == ceil(len(word) / 2) or 0 < len(word) <= 2:
#         return True

#     while low_index < ceil(len(word) / 2):
#         if word[low_index] == word[high_index]:
#             return is_palindrome_recursive(word, low_index + 1, high_index - 1)
#         else:
#             return False
