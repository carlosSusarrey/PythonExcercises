# Chapter1 problem3
import collections


def urlify_string(input_string: collections.Iterable, true_length: int):
    char_array = list(input_string)
    space_counter = 0

    for i in range(0, true_length-1):
        if char_array[i] == ' ':
            space_counter += 1

    index = true_length + space_counter * 2

    for i in range(true_length -1 , 0, -1):
        if char_array[i] == ' ':
            char_array[index - 1] = '0'
            char_array[index - 2] = '2'
            char_array[index - 3] = '%'
            index -= 3
        else:
            char_array[index - 1] = char_array[i]
            index -= 1

    print(char_array)

urlify_string('Mr John Smith    ',13)