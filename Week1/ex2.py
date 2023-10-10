string = input("Enter a string: ")
vowels = ["a", "e", "i", "o", "u"]
vowel_count = 0
for i in string:
    if i in vowels:
        vowel_count += 1

print(f"Num of vowels in string {string} is {vowel_count}")
