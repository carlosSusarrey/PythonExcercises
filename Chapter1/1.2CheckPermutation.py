# Chapter1 problem 2
import collections


def check_if_strings_are_permutations(input_string1: collections.Iterable, input_string2: collections.Iterable):
    dictionary = {}

    for letter in input_string1:
        dictionary[letter] = 0

    for letter in input_string2:
        dictionary[letter] = 0

    for letter in input_string1:
        if letter != ' ':
            dictionary[letter] = 1

    for letter in input_string2:
        if letter != ' ':
            dictionary[letter] = dictionary[letter]-1

    for letter in dictionary:
        if dictionary[letter] != 0:
            return False

    return True


def check_if_strings_are_permutations_without_hash(input_string1: collections.Iterable, input_string2: collections.Iterable):
    if len(input_string2) != len(input_string1):
        return False

    input_string1 = ''.join(sorted(input_string1))
    input_string2 = ''.join(sorted(input_string2))

    for i in range(len(input_string1)):
        if input_string1[i] != input_string2[i]:
            return False

    return True


print(check_if_strings_are_permutations("holmd     a","al  fgf ohmd"))
print(check_if_strings_are_permutations_without_hash("ecanim","camine"))