def get_first_n_fibonnaci_numbers(number_index):
    fibbonaci_sequence = [0, 1]
    for i in range(2, number_index):
        fibbonaci_sequence.append(fibbonaci_sequence[i - 1] + fibbonaci_sequence[i - 2])
    return fibbonaci_sequence


print(get_first_n_fibonnaci_numbers(10))
