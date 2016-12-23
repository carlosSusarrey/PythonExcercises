# Chapter 1 problem 4
import collections


def is_palindrome_of_permutation(input_string: collections.Iterable):
    alphabet = {}

    for character in input_string:
        if character != ' ':
            alphabet[character] = 0

    for character in input_string:
        if character != ' ':
            alphabet[character] += 1

    odd_count = 0
    for character in alphabet:
        if alphabet[character] % 2 != 0:
            if odd_count > 0:
                return False
            odd_count += 1

    return True

print (is_palindrome_of_permutation('tact coal'))