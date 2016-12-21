# Chapter 1 problem 5
import collections


def one_way(input_string1, input_string2):

    string1_length = len(input_string1)
    string2_length = len(input_string2)

    size_difference = abs(string1_length - string2_length)

    if 1 < size_difference:
        return False

    if string1_length > string2_length:
        long_string = input_string1
        short_string = input_string2
    else:
        long_string = input_string2
        short_string = input_string1

    differences = 0
    longer_string_iterator = 0

    for i in range(0, len(short_string)):
        if short_string[i] != long_string[longer_string_iterator]:
            differences += 1

            if differences > 1:
                return False

            if size_difference != 0:
                longer_string_iterator += 1
                if short_string[i] != long_string[longer_string_iterator]:
                    return False
        longer_string_iterator += 1
    return True

print(one_way("pale","ple"))
print(one_way("pales","pale"))
print(one_way("pale","bale"))
print(one_way("pale","bake"))