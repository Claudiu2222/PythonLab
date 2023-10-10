def count_bits_of_value_one(number):
    count = 0
    while number:
        if number & 1:
            count += 1
        number >>= 1
    return count


print(count_bits_of_value_one(255))
