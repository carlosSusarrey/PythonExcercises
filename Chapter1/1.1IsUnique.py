# Chapter 1 problem 1
import collections


def has_all_unique_characters(input_string: collections.Iterable) -> object:

    alphabet = {}

    for character in input_string:
        alphabet[character] = 0

    for character in input_string:
        if alphabet[character] > 0:
            return False
        alphabet[character] = 1

    return True


def has_all_unique_characters_no_additional_structures(input_string: collections.Iterable) -> object:
    input_string = ''.join(sorted(input_string))

    for i in range(0, len(input_string) - 1):
        if input_string[i] == input_string[i + 1]:
            return False

    return True


print(has_all_unique_characters("helo"))
print(has_all_unique_characters_no_additional_structures("helo"))