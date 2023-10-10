string1 = input()
string2 = input()
count = 0

# print(string2.count(string1)) pt abab si ababab afiseaza 1

for i in range(len(string2) - len(string1) + 1):
    if string2[i : i + len(string1)] == string1:
        count += 1

print(count)
