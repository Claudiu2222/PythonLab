def reversed_number(number):
    temp = 0
    while number != 0:
        temp = temp * 10 + number % 10
        number //= 10
    return temp


def is_palindrome(number):
    if number == reversed_number(number):
        return True
    return False


print(is_palindrome(3232323))
print(is_palindrome(321))
print(is_palindrome(12211))
