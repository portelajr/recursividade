def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    present_students = 0

    for student in permanence_period:
        if type(student[0]) is not int or type(student[1]) is not int:
            return None

        if (student[0] <= target_time <= student[1]) is True:

            present_students = present_students + 1
    return present_students

# https://stackoverflow.com/questions/32770725/how-to-check-a-specific-type-of-tuple-or-list
# https://www.programiz.com/python-programming/methods/built-in/isinstance

# entrada = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
