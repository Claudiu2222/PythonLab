def compute_characters_divisible_by_x(list_of_strings, x=1, flag=True):
    returned_list = []
    for string in list_of_strings:
        current_string_char_set = set()
        for char in string:
            if flag:
                if ord(char) % x == 0:
                    current_string_char_set.add(char)
            else:
                if ord(char) % x != 0:
                    current_string_char_set.add(char)
        returned_list.append(list(current_string_char_set))
    return returned_list


print(compute_characters_divisible_by_x(["test", "hello", "lab002"], x=2, flag=False))
