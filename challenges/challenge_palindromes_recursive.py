def is_palindrome_recursive(word, low_index, high_index):

    limit_iteractions = 0

    if limit_iteractions == len(word) // 2:
        return True

    while limit_iteractions < len(word) // 2:
        # if (high_index - low_index) < 2:
        #     limit_iteractions = limit_iteractions + 1
        #     return is_palindrome_recursive(word, low_index, high_index)
        if word[low_index] == word[high_index]:
            limit_iteractions = limit_iteractions + 1
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        else:
            return False
