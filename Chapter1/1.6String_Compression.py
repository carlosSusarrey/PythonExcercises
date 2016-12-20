# Chapter 1 problem 6
def string_compression(input_string):

    string_length = len(input_string)
    aux_string = ""

    current_letter = input_string[0]
    current_count = 1
    aux_string += current_letter

    for i in range(1, string_length):
        if current_letter != input_string[i]:
            aux_string += str(current_count)
            current_count = 0
            current_letter = input_string[i]
            aux_string += current_letter

        current_count += 1

    aux_string += str(current_count)
    if len(aux_string) > len(input_string):
        return input_string
    return aux_string

print(string_compression("aaaaaaabbbbbbcccccccccbbbbbbbbddddddAAAAAAAAbbbbbbbeeeeeee$$$$$$@@@@@@@@hbfhjn"))