# Chapter 1 problem 9


def is_rotation(input_string1, input_string2):
    if len(input_string1) != len(input_string2):
        return False
    input_string1 += input_string1
    if input_string2 in input_string1:
        return True
    return False


print(is_rotation("muchacho", "chachomu"))