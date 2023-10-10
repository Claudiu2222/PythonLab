def find_most_common_letter(string):
    string = string.lower()
    most_common_letter = ""
    max_count = 0
    letters_set = set(string)
    for i in letters_set:
        if i.isalpha() and ((current_count := string.count(i)) > max_count):
            max_count = current_count
            most_common_letter = i
    return most_common_letter


print(find_most_common_letter("An Apple is not a tomato"))
