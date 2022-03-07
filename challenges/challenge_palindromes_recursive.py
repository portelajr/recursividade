def is_palindrome_recursive(word, low_index, high_index):

    limit_iteractions = 0

    if limit_iteractions == int(len(word) // 2):
        return True

    while limit_iteractions < len(word) // 2:
        equality = word[low_index] == word[high_index]
        if (high_index - low_index) <= 2 and equality:
            limit_iteractions = limit_iteractions + 1
            return is_palindrome_recursive(word, low_index, high_index)
        if equality is True:
            limit_iteractions = limit_iteractions + 1
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        else:
            return False
