# Chapter 1 problem 4
import collections


def is_palindrome_of_permutation(input_string: collections.Iterable):
    hash_table = {}

    for letter in input_string:
        if letter != ' ':
            hash_table[letter] = 0

    for letter in input_string:
        if letter != ' ':
            hash_table[letter] += 1

    odd_count = 0
    for integer in hash_table:
        if hash_table[integer] % 2 != 0:
            if odd_count > 0:
                return False
            odd_count += 1

    return True

print (is_palindrome_of_permutation('tact coal'))