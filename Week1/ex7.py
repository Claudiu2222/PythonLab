def extract_first_number_from_string(string):
    found_number = ""
    for i in range(len(string)):
        if string[i].isdigit():
            if i != 0 and string[i - 1] == "-":
                found_number += "-"
            found_number += string[i]
            if i + 1 == len(string) or not string[i + 1].isdigit():
                break
    return int(found_number)


string = "abc-123abc"
print(extract_first_number_from_string(string))
