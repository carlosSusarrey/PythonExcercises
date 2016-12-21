# Chapter1 problem 2
import collections


def check_if_strings_are_permutations(input_string1: collections.Iterable, input_string2: collections.Iterable):
    alphabet = {}

    for character in input_string1:
        alphabet[character] = 0

    for character in input_string2:
        alphabet[character] = 0

    for character in input_string1:
        if character != ' ':
            alphabet[character] = 1

    for character in input_string2:
        if character != ' ':
            alphabet[character] = alphabet[character]-1

    for character in alphabet:
        if alphabet[character] != 0:
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