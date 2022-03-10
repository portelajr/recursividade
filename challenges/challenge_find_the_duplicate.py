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


def find_duplicate(nums):
    sorted_array = merge_sort(nums)
    # max_i = (len(sorted_array) - 1)
    # duplicated = ""
    for i in range(1, len(sorted_array)):
        if sorted_array[i] == sorted_array[i - 1]:
            print(sorted_array[i])
            return sorted_array[i]

    return False

# print(find_duplicate([1, 3, 5, 4, 7, 9]))
