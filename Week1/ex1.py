number_of_entries = int(input("Num of entries: "))
entries = []
for i in range(number_of_entries):
    entries.append(int(input(f"Enter number {i+1}: ")))


def find_gcd_of_entries(entries, number_of_entries):
    if number_of_entries == 1:
        return entries[0]
    current_gcd = gcd(entries[0], entries[1])
    for i in range(2, number_of_entries):
        current_gcd = gcd(entries[i], current_gcd)
    return current_gcd


def gcd(a, b):
    if a == b:
        return b
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


print(find_gcd_of_entries(entries, number_of_entries))
