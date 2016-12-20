# Chapter 1 problem 1
import collections


def has_all_unique_characters(input_string: collections.Iterable) -> object:

    my_array = {}

    for letter in input_string:
        my_array[letter] = 0

    for letter in input_string:
        if my_array[letter] > 0:
            return False
        my_array[letter] = 1

    return True


def has_all_unique_characters_no_additional_structures(input_string: collections.Iterable) -> object:
    input_string = ''.join(sorted(input_string))

    for i in range(0, len(input_string) - 1):
        if input_string[i] == input_string[i + 1]:
            return False

    return True


print(has_all_unique_characters("helo"))
print(has_all_unique_characters_no_additional_structures("helo"))