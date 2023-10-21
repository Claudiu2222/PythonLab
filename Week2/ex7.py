def is_palindrome(number):
    number_string = str(number)
    if number_string == number_string[::-1]:
        return True
    return False


def get_palindrome_tuple(number_list):
    max_palindrome = -1
    number_of_palindromes = 0

    for number in number_list:
        if is_palindrome(number):
            number_of_palindromes += 1
            if number > max_palindrome:
                max_palindrome = number
    if number_of_palindromes == 0:
        return (0, "No palindromes found")
    return (number_of_palindromes, max_palindrome)


print(get_palindrome_tuple([1, 10, 11, 13, 22, 25, 99, 101, 3, 3]))
