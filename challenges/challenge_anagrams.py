def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    return merge(left, right, array.copy())


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):

        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def is_anagram(first_string, second_string):

    if len(first_string) == 0 or len(second_string) == 0:
        return False

    if len(first_string) != len(second_string):
        return False

    char_list_first = list(first_string)
    char_list_second = list(second_string)
    sorted_chars_first = merge_sort(char_list_first)
    sorted_chars_second = merge_sort(char_list_second)

    for index, letter in enumerate(sorted_chars_first):
        if sorted_chars_first[index] != sorted_chars_second[index]:
            return False
    return True
