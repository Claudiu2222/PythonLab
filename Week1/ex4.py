string = "TestPentruLaboratorulUnuTEST"

current_index = 0
array_of_substrings = []
for i in range(1, len(string)):
    if string[i].isupper():
        array_of_substrings.append(string[current_index:i])
        current_index = i
array_of_substrings.append(string[current_index:])

print(("_".join(array_of_substrings)).lower())
